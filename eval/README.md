# LogicVista Evaluation

## Overview
This directory contains the necessary tools and instructions for evaluating MLLMs using the LogicVista dataset. Our evaluation framework assesses models across multiple logical reasoning tasks, providing insights into their capabilities and limitations.

## Getting Started
1. **Setup**: Ensure you have Python installed and the necessary dependencies by running `pip install -r requirements.txt` (ensure you create this file based on your script dependencies).
2. **Running Evaluations**: Use the `run.sh` script to start the evaluation process, which automatically processes the dataset and compares model outputs against the provided answers.
3. **Analyzing Results**: After running evaluations, use `analyze_accuracy.py` to summarize the accuracy across different reasoning tasks.

## Directory Structure
- `analyze_accuracy.py`: Script for analyzing model performance.
- `constants.py`: Contains constants used in evaluation scripts.
- `run.sh`: Bash script to run the entire evaluation pipeline.
- `extract_accuracy_new.py`: Script to extract and process accuracy from raw model outputs.
- `answers/`: Contains answer files for various MLLMs, formatted as JSON.
- `results/`: Location where the evaluation results will be saved.

## Using the Evaluation Scripts
Detailed instructions on using each script can be found within their respective file headers. Generally, the process is as follows:
- **Preparation**: Place your model's output in the `answers/` directory, following the naming convention `[model_name]-answers.json`.
- **Execution**: Run `./run.sh` to start the evaluation. Adjust the script as needed to match your environment.
- **Analysis**: Execute `python analyze_accuracy.py` to generate accuracy metrics. Results are saved in the `results/` directory.

## Example: Evaluating GPT4
To evaluate a model, such as GPT4, using the LogicVista evaluation framework, follow these steps:
1. Prepare the GPT4 output results and ensure they are named `GPT4-answers.json`. Place this file in the `answers/` directory.
2. Update the `constants.py` file to set the `$MODEL` variable to `GPT4`.
3. Run the evaluation by executing the `run.sh` script. This script processes the GPT4 answers, compares them against the correct answers, and generates an accuracy report.
