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

# creating memory of used answers
answers = []

# ==================== functions ====================


def prompt_gen():
    """
    Return a word at random as a prompt
        Returns:
            prompt (str): word prompt
    """
    return random.choice(words)


def answer_in():
    """
    #TODO 
    """
    while True:
        ans = input()
        if ans in answers:
            print("Used word. Try again.")
            continue
        if ans in all_synsets:
            break
        else:
            print("Invalid word. Try again.")
    answers.append(ans)
    return ans


def scoring(word1, word2):
    sims = []
    for synset1 in wd.synsets(word1):
        for synset2 in wd.synsets(word2):
            sims.append(
                synset1.path_similarity(synset2))
    sim = sum(sims) / len(sims)
    points = round((1-sim)*10, 2)
    return points


def score_update(score, points):
    print(f"+ {points:.1f} points")  # display points
    score_new = score + points
    print(f"Score: {score_new:.1f}")  # display score_new
    return score_new


def main():
    score = 0
    prompt = prompt_gen()
    while score < 100:
        print(prompt)
        answer = answer_in()
        points = scoring(prompt, answer)
        score = score_update(score, points)
        if score >= 100:
            break
        prompt = answer
    print("You did it! Your Train of Thoughts has been all over the place!")


if __name__ == "__main__":
    main()
