#!/usr/bin/env python3
# open AI key
APIKEY = ""

# ONLY CHANGE THE MODEL OPTION TO CHANGE EXTRACTION TYPES --> affects all files
# Model Options (case sensitive):
# LLAVA7B
# LLAVA13B
# otter9B
# GPT4
# BLIP2
# GIT
# GIT-large
# LLAVANEXT-7B-mistral
# LLAVANEXT-7B-vicuna
# LLAVANEXT-13B-vicuna
# LLAVANEXT-34B-NH
# deplot
# matcha-base
# miniGPTvicuna7B
# miniGPTvicuna13B
# pix2struct
# instructBLIP-vicuna-7B
# instructBLIP-vicuna-13B
# instructBLIP-flan-t5-xl
# instructBLIP-flan-t5-xxl
MODEL = "instructBLIP-vicuna-13B"

# file paths for where MLLM answers are stored and where accuracy result files are stored
ANSWERS_PATH = "answers/" + MODEL + "-answers.json"
RESULTS_PATH = "results/" + MODEL + "-accuracy-results.csv"
DATASET_PATH = "/home/edwardsun/Documents/Code/ScAI/MLLM/MLR_dataset/"
