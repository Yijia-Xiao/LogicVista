# LogicVista Dataset

## Overview
The LogicVista dataset is designed to evaluate the logical reasoning abilities of MLLMs in visual contexts. It features 448 visual multiple-choice questions, each annotated with detailed image-instruction-solution-reasoning pairs, across five categories of logical reasoning.

## Dataset Structure
- `dataset.json`: A comprehensive JSON file containing all the questions, options, correct answers, and explanations.
- `images/`: A directory containing all the images referenced in `dataset.json`.

## Using the Dataset
To use the dataset for model training or evaluation, load `dataset.json` into your preferred data processing library. The file structure is as follows:

```
{
    "v1_0": {
        "imagename": "v1_0.png",
        "question": "What choice (A, B, C, or D) should be in place of the question mark that fits the pattern?",
        "answer": "C",
        "reasoning": "The dot is constantly found in each of the three sequences but the square moves one square each time (to the right or left). In the third sequence, we can see that the square moves to the right, leading to the conclusion that the missing figure is found in answer C.",
        "skill": [
            "inductive"
        ],
        "capability": [
            "diagram",
            "ocr"
        ],
        "imagesource": "aptitudetests",
        "sourcelink": "https://www.aptitudetests.org/logical-reasoning-test/"
    },
    ...
}
```