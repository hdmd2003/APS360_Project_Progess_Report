import pandas as pd
import numpy as np

data = pd.read_excel("CLEAR_corpus_final.xlsx")

excerpt = data["Excerpt"][0]

def syllable_count(word):
    '''
    Adapted from Stackoverflow to count syllables in a word, see link
    https://stackoverflow.com/questions/46759492/syllable-count-in-python:
    '''
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def flesch(excerpt):
    '''
    Algo I made to calculate the Flesch score for a given excerpt (correct within error of 1/80)
    '''
    excerpt = excerpt.replace(",", " ")
    excerpt = excerpt.replace("!", ".")
    excerpt = excerpt.replace("?", ".")

    total_syllables = 0

    for sentence in excerpt.split("."):
        sentence = sentence.lstrip().rstrip()
        for word in sentence.split(" "):
            word = word.lstrip().rstrip()
            if word == "":
                pass
            else:
                total_syllables += syllable_count(word)

    return 206.835 - 1.015 * len(excerpt.split(" "))/len(excerpt.split(".")) - 84.6 * (total_syllables/len(excerpt.split(" ")))

print("Flesch Score:", flesch(excerpt))


def find_neighbours(value, df, colname):
    '''
    Function from Stackoverflow to find neighbors to a value from the Flesch function.
    Will give me the index of the closest BST values.
    '''
    exactmatch = df[df[colname] == value]
    if not exactmatch.empty:
        return exactmatch.index
    else:
        lowerneighbour_ind = df[df[colname] < value][colname].idxmax()
        upperneighbour_ind = df[df[colname] > value][colname].idxmin()
        return [lowerneighbour_ind, upperneighbour_ind]

ind_1, ind_2 = find_neighbours(flesch(excerpt), data, "Flesch-Reading-Ease")

predicted_bt = (float(data.loc[[ind_1]]["BT_easiness"]) + float(data.loc[[ind_2]]["BT_easiness"]))/2

print("Predicted BT Score:", predicted_bt)
