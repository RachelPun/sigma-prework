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


def prompt_gen():
    """
    Return a word at random as a prompt
        Returns:
            prompt (str): word prompt
    """
    return random.choice(words)


def answer_in(answers):
    """
    #TODO 
    """
    while True:
        ans = input()
        if ans in answers:
            print(f"{ans}: used word. Try again.")
            continue
        if ans in all_synsets:
            break
        else:
            print(f"{ans}: Invalid word. Try again.")
    answers.append(ans)
    return ans, answers


def scoring(word1, word2):
    sims = []
    for synset1 in wd.synsets(word1):
        for synset2 in wd.synsets(word2):
            sims.append(
                synset1.path_similarity(synset2))
    sim = sum(sims) / len(sims)
    points = round((1-sim)**3*10, 1)
    return points


def score_update(score, points):
    print(f"+ {points} points")  # display points
    score_new = score + points
    print(f"Score: {score_new}")  # display score_new
    return score_new


def game():
    score = 0
    prompt = prompt_gen()
    answers = [prompt]  # memory of used answers
    while score < 100:
        print(prompt)
        answer, answers = answer_in(answers)
        points = scoring(prompt, answer)
        score = score_update(score, points)
        if score >= 100:
            break
        prompt = answer
    print("You did it! Your Train of Thoughts has been all over the place!")


def intro():
    instructions = """
"""
    print(instructions)

# def game_start():

# def game_restart():


def main():
    # intro()
    game()
    # game_start()
    # game_restart()


if __name__ == "__main__":
    main()
