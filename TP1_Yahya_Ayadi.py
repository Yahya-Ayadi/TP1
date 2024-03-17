"""
File: TP1_Yahya_Ayadi.py
Author: Yahya Ayadi
TP: 1

"""

#Exercices 1&2:

# The following function generates a list of French words from a dictionary file, but you have to change the path
#of 'motspossibles.dic'

def Generate_lexicon():
    f = open("C:/Users/PC/motspossibles.dic", 'r')  # Change the path of 'motspossibles.dic'
    frenchwords = list()
    lines = f.readlines()
    for line in lines:
        frenchwords.append(line.strip())
    return frenchwords

# This auxiliary function checks whether the word 'mot' is composed of letters from the "tirage" list

def word_in_tirage(word,tirage):
    t=tirage.copy()
    for l in word:
        if l not in t:
            return False
        t.remove(l)
    return True

# The following function generates the list of possible words extracted from the lexicon,
# eliminating words that use letters not present in the "tirage" list


def possible(tirage):
    frenchwords = Generate_lexicon()
    mots_possibles = []
    for el in frenchwords:
        if word_in_tirage(el, tirage):
            mots_possibles.append(el)
    return mots_possibles

# This function returns the longest word from the "possible" list, taking 'tirage' in argument
def longest_word(tirage):
    possible_words = possible(tirage)
    solution = possible_words[0]
    for word in possible_words:
        if len(word) > len(solution):
            solution = word
    return solution


#Exercice 3:

#1- We choose a dictionary to represent the points associated with letters

points_lettres = {
    'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'd': 2, 'g': 2, 'm': 2,
    'b': 3, 'c': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4,
    'j': 8, 'q': 8,
    'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}
#2-The following function returns the score of the word in argument
def score(mot):
    s=0
    for el in mot:
        s+=points_lettres[el]
    return s
#3-max_score returns the word that has the maximum points and the value of the maximum points
def highest_score(list_mot):
    mot_max = list_mot[0]
    score_max = score(list_mot[0])
    for mot in list_mot:
        if score(mot) > score_max:
            mot_max = mot
            score_max = score(mot)
    return (mot_max,score_max)

#4-the following function returns the highest_score word possible from 'tirage'
def research_max_point(tirage):
    list_mot=possible(tirage)
    return highest_score(list_mot)

#Exercice4:

def max_score(letters):
    """
    This function returns the word having the highest score and its score.
    This word can be written by letters in letters (including the
    joker).

    :letters: A list of string
    :return: A list of string and integer

    """
    joker = '?'
    if joker not in letters:
        return highest_score(list(letters))
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        positionjoker = letters.find('?')
        words = []
        for letter in alphabet:
            listletter = list(letters)
            listletter[positionjoker] = letter
            words += possible(listletter)
    return (highest_score(words)[0], highest_score(words)[1] - 1)

print('===========================\n'
      '==Exercice1. Longest word==\n'
      '===========================\n')
print("possible(['b', 'p', 'd', 'w', 's']) = "
      f"{possible(['b', 'p', 'd', 'w', 's', 'y', 'w'])}\n"
      "Expected result: ['bd', 'y']")
print(f"longest_word(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i']) = "
      f"{longest_word(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i'])}\n"
      "Expected result: bis")
print('===========================\n'
      '==Exercice3 Highest score==\n'
      '===========================\n')
print(f"score('a') = {score('a')}\n"
      "Expected result: 1")
print(f"score('manger') = {score('manger')}\n"
      "Expected result: 8")
print(f"highest_score(['rte', 'ver', 'ce', 'etc', 'cet', 'ex']) = "
      f"{highest_score(['rte', 'ver', 'ce', 'etc', 'cet', 'ex'])}\n"
      "Expected result: ('ex', 11)")
print(f"highest_score(['m','a', 'n','g','e','r']) = "
      f"{highest_score(['m','a', 'n','g','e','r'])}\n"
      "Expected result: ('gramen', 8) or ('manger', 8)")
print(f"research_max-point(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i']) = "
      f"{research_max_point(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j'])}")
print('===========================\n'
      '==Exercice4 Highest score==\n'
      '===========================\n')
print(f"max_score('zxcvrrt?') = {max_score('zxcvrrt?')}\n"
      "Expected result: ('czar', 14)")


