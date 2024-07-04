#!/usr/bin/env python3
import json
import sys
import os
import pandas as pd
import constants
from tqdm import tqdm
import re
# chatgpt has knowledge of world
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from pydantic import BaseModel, Field, field_validator
from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain.output_parsers import RetryWithErrorOutputParser
from langchain.chat_models import ChatOpenAI

# ONLY CHANGE THE MODEL OPTION TO CHANGE EXTRACTION TYPES
# Model Options (case sensitive):
# LLAVA


class Answer(BaseModel):
    choices: list[str] = Field(
        description="multiple choice answer of a list of letters or numbers chosen by the given text"
    )

    @field_validator("choices")
    def validate_choices(cls, value):
        if not isinstance(value, list):
            raise ValueError("Choices must be a list")
        return value


# constants
os.environ["OPENAI_API_KEY"] = constants.APIKEY

temperature = 0.2
# output structure

# llm for
llm = ChatOpenAI(model="gpt-4", temperature=temperature)

parser = PydanticOutputParser(pydantic_object=Answer)
format_instructions = parser.get_format_instructions()

# read the truth file
ground_truth_file = open(constants.DATASET_PATH + "dataset.json", "r", encoding="utf-8")
ground_truth = json.loads(ground_truth_file.read())
# load json answers from a given mllm
data_file = open(constants.ANSWERS_PATH, "r", encoding="utf-8")
print("Ground Truth Length: " + str(len(ground_truth)))
data = json.loads(data_file.read())
print("Data Length: " + str(len(data)))


# output dataframe
df = pd.DataFrame(
    columns=[
        "id",
        "reasoning skill",
        "capability",
        "true answer",
        (constants.MODEL + " Answer"),
        "match?",
    ]
)
df = pd.DataFrame()

for i in tqdm(range(0, len(data))):
    id = "v1_" + str(i)

    # answer entry----------
    entry = ""
    if "ASSISTANT:" in data[id]["answer"]:
        entry = data[id]["answer"].split("ASSISTANT:")[1]
    else:
        entry = data[id]["answer"]
    question = ground_truth[id]["question"]

    # only use GPT parse if already not one letter answers
    #
    MLLM_answers = [entry.strip()]
    if len(entry.strip()) != 0:
        # if length is 1 with only letters and isn't abcde
        if (len(entry.strip()) == 1 and entry.strip().isalpha() and entry.strip().lower() not in 'abcde') or (len(entry.strip()) == 1 and not entry.strip().isalpha() and not entry.strip().isnumeric()):
            MLLM_answers = ['ZZZZZ']
        else:
            template = """
            You are a information extractor that extracts multiple choice letter answer choices
                from a paragraph that contains the answer choice and sometimes and explaination of why that choice is correct to the following question: \"{question}\"\n
                What letter did the following answer choose? If the answer did not select a letter answer choice, first try to infer the answer based off the given choices.
                If it does not seem like the given answer corresponds to an answer choice OR if there is no selected answer, please just respond with the string ZZZZZ.
                Make sure you answer with ONLY the letters chosen.\nHere is what I need you to extract from:\nThe answer is \"{entry}\"\n{format_instructions}
            Helpful Answer:
            """
            prompt_template = PromptTemplate.from_template(template)
            prompt_template = prompt_template.format(
                question=question, entry=entry, format_instructions=format_instructions
            )
            output = llm.invoke(prompt_template).content
            output_choices = ""
            # ensure formatting correctly
            success = False
            for i in range(0, 100):
                try:
                    # try parse
                    output_choices = parser.parse(output)
                    output_choices.choices
                    success = True
                    break
                except Exception:
                    try:
                        fixing_parser = OutputFixingParser.from_llm(
                            parser=parser, llm=OpenAI(temperature=0.3)
                        )
                        misformatted = str(output)
                        output_choices = fixing_parser.parse(misformatted)
                    except Exception:
                        continue
            if (not success):
                for i in range(0, 100):
                    try:
                        # try parse
                        output_choices = parser.parse(output)
                        output_choices.choices
                        success = True
                        break
                    except Exception:
                        try:
                            retry_parser = RetryWithErrorOutputParser.from_llm(parser=parser, llm=OpenAI(temperature=0.7))
                            prompt_value = prompt.format_prompt(text=entry)
                            output_choices = retry_parser.parse_with_prompt(output, prompt_value)
                        except Exception:
                            continue
            if (success):
                # answer choices array from MLLM
                MLLM_answers = output_choices.choices
            else:
                MLLM_answers = ['ZZZZZ'] 

    # ground truth answers matching?
    truth_answers = ground_truth[id]["answer"].split(", ")
    match = 0
    for j in range(0, len(MLLM_answers)):
        MLLM_answers[j] = MLLM_answers[j].lower()
    for j in range(0, len(truth_answers)):
        truth_answers[j] = truth_answers[j].lower()

    # must hard equal to pass --> both should be in alphabetical order
    MLLM_answers.sort()
    truth_answers.sort()
    if MLLM_answers == truth_answers:
        match = 1

    row = pd.DataFrame(
        {
            "id": [id],
            "reasoning skill": [ground_truth[id]["skill"]],
            "capability": [ground_truth[id]["capability"]],
            "true answer": [truth_answers],
            (constants.MODEL + " answer extracted"): [MLLM_answers],
            (constants.MODEL + " answer raw"): [entry],
            "match?": [match],
        }
    )
    df = pd.concat([df, row], ignore_index=True)

df.to_csv(constants.RESULTS_PATH)
