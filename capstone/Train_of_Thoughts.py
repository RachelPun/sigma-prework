# ==================== imports ====================
# !python3 -m pip install --upgrade pip
# !pip3 install openpyxl
import openpyxl
import pandas as pd
from IPython.display import display
from nltk.corpus import wordnet as wd
import random

# ==================== word list ====================
# creating word list for prompts
words_df = pd.read_excel(
    "https://www.wordfrequency.info/samples/wordFrequency.xlsx", sheet_name="1 lemmas")
words_df = words_df[["lemma", "PoS"]]
words_df = words_df[words_df["PoS"].isin(["n", "v", "j"])]
words = words_df["lemma"].to_list()
all_synsets = set(wd.all_lemma_names())

# ==================== functions ====================


def prompt():
    return random.choice(words)


def answer():
    while True:
        ans = input()
        if ans in all_synsets:
            break
        else:
            print("Invalid word. Try again.")
    return ans


def scoring(word1, word2):
    sim = []
    for synset1 in wd.synsets(word1):
        for synset2 in wd.synsets(word2):
            sim.append(
                synset1.path_similarity(synset2))
    sim = sum(sim) / len(sim)
    score = (1-sim)*10
    return score


prompt = prompt()
print(prompt)
answer = answer()
print(answer)

print(scoring(prompt, answer))
