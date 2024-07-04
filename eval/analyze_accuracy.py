#!/usr/bin/env python3
import pandas as pd
import constants
from colorama import Fore, Back, Style

df = pd.read_csv(constants.RESULTS_PATH)
df_tot = df

# type of reasoning
df_inductive = df[df["reasoning skill"].str.contains("inductive")]
df_deductive = df[df["reasoning skill"].str.contains("deductive")]
df_numerical = df[df["reasoning skill"].str.contains("numerical")]
df_spatial = df[df["reasoning skill"].str.contains("spatial")]
df_mechanical = df[df["reasoning skill"].str.contains("mechanical")]

# capability
df_diagram = df[df["capability"].str.contains("diagram")]
df_ocr = df[df["capability"].str.contains("ocr")]
df_diagram_and_ocr = df[
    df["capability"].str.contains("ocr") & df["capability"].str.contains("diagram")
]

# percent accuracies
# reasoning skill
print(Fore.RED + "Model: " + constants.MODEL + Fore.WHITE)
print(Fore.GREEN + "Reasoning Skill Acc:" + Fore.WHITE)
tot_correct = df_tot["match?"].sum()
tot_acc = (tot_correct / df_tot.shape[0]) * 100
print(
    "Total: "
    + str(tot_acc)
    + "%"
    + "\t"
    + "("
    + str(tot_correct)
    + "/"
    + str(df_tot.shape[0])
    + ")"
)

inductive_correct = df_inductive["match?"].sum()
inductive_acc = (inductive_correct / df_inductive.shape[0]) * 100
print(
    "Inductive: "
    + str(inductive_acc)
    + "%"
    + "\t"
    + "("
    + str(inductive_correct)
    + "/"
    + str(df_inductive.shape[0])
    + ")"
)

deductive_correct = df_deductive["match?"].sum()
deductive_acc = (deductive_correct / df_deductive.shape[0]) * 100
print(
    "Deductive: "
    + str(deductive_acc)
    + "%"
    + "\t"
    + "("
    + str(deductive_correct)
    + "/"
    + str(df_deductive.shape[0])
    + ")"
)

numerical_correct = df_numerical["match?"].sum()
numerical_acc = (numerical_correct / df_numerical.shape[0]) * 100
print(
    "Numerical: "
    + str(numerical_acc)
    + "%"
    + "\t"
    + "("
    + str(numerical_correct)
    + "/"
    + str(df_numerical.shape[0])
    + ")"
)

spatial_correct = df_spatial["match?"].sum()
spatial_acc = (spatial_correct / df_spatial.shape[0]) * 100
print(
    "Spatial: "
    + str(spatial_acc)
    + "%"
    + "\t"
    + "("
    + str(spatial_correct)
    + "/"
    + str(df_spatial.shape[0])
    + ")"
)

mechanical_correct = df_mechanical["match?"].sum()
mechanical_acc = (mechanical_correct / df_mechanical.shape[0]) * 100
print(
    "Mechanical: "
    + str(mechanical_acc)
    + "%"
    + "\t"
    + "("
    + str(mechanical_correct)
    + "/"
    + str(df_mechanical.shape[0])
    + ")"
)

# capability
print(Fore.GREEN + "Capability Acc:" + Fore.WHITE)
diagram_correct = df_diagram["match?"].sum()
diagram_acc = (diagram_correct / df_diagram.shape[0]) * 100
print(
    "Diagram: "
    + str(diagram_acc)
    + "%"
    + "\t"
    + "("
    + str(diagram_correct)
    + "/"
    + str(df_diagram.shape[0])
    + ")"
)

ocr_correct = df_ocr["match?"].sum()
ocr_acc = (ocr_correct / df_ocr.shape[0]) * 100
print(
    "OCR: "
    + str(ocr_acc)
    + "%"
    + "\t"
    + "("
    + str(ocr_correct)
    + "/"
    + str(df_ocr.shape[0])
    + ")"
)

df_diagram_and_ocr_correct = df_diagram_and_ocr["match?"].sum()
df_diagram_and_ocr_acc = (
    df_diagram_and_ocr_correct / df_diagram_and_ocr.shape[0]
) * 100

print(
    "OCR and Diagram: "
    + str(df_diagram_and_ocr_acc)
    + "%"
    + "\t"
    + "("
    + str(df_diagram_and_ocr_correct)
    + "/"
    + str(df_diagram_and_ocr.shape[0])
    + ")"
)
