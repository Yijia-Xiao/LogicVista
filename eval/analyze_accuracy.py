import pandas as pd
import constants
from colorama import Fore, Back, Style

cat = ["diagram", "ocr", "patterns", "graphs", "tables", "3d shapes", "puzzles", "sequences", "physics"]

df = pd.read_csv(constants.RESULTS_PATH)
df_tot = df


df_inductive = df[df["reasoning skill"].str.contains("inductive")]
df_deductive = df[df["reasoning skill"].str.contains("deductive")]
df_numerical = df[df["reasoning skill"].str.contains("numerical")]
df_spatial = df[df["reasoning skill"].str.contains("spatial")]
df_mechanical = df[df["reasoning skill"].str.contains("mechanical")]

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
for i in cat:
    curr = df[df["capability"].str.contains(i.replace(" ", ""))]
    correct = curr["match?"].sum()
    acc = (correct / curr.shape[0]) * 100
    print(
        f"{i}: "
        + str(acc)
        + "%"
        + "\t"
        + "("
        + str(correct)
        + "/"
        + str(curr.shape[0])
        + ")"
    )
