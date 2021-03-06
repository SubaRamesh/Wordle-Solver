import re, json, requests, csv, os
import pandas as pd
import matplotlib.pyplot as plt


# load words (only 5 letters)
f = open('guess_dictionary.json')
guess_words = json.load(f)
f.close()

f2 = open('solution_dictionary.json')
solution_words = json.load(f2)
f2.close()

f1 = open('letterFreq.json')
letter_frequency = json.load(f1)
f1.close()


# updates wordList with information from last guessed word
def updateWithGuess(wordList, guess, guessResult):
    newWords = set(wordList)
    
    for word in wordList:
        for i in range(len(guess)):
            if guessResult[i] == 'G' and guess[i] != word[i] and word in newWords:
                # pattern[i] = guess[i]
                newWords.remove(word)
                break
            elif guessResult[i] == 'X' and guess[i] in word and word in newWords:
                # rejectedLetters.add(guess[i])
                newWords.remove(word)
                break
            elif guessResult[i] == 'Y' and guess[i] not in word and word in newWords:
                # letters.add[guess[i]]
                newWords.remove(word)
                break
            elif guessResult[i] == 'Y' and guess[i] == word[i] and word in newWords:
                newWords.remove(word)
                break
    
    # print(newWords)
    return newWords
            
    
# produce result for word from known answer    
def create_result(word, solution):
    res = ""
    
    for i in range(len(solution)):
        if word[i] not in solution:
            res += 'X'
        elif word[i] == solution[i]:
            res += 'G'
        else:
            res += 'Y'
    
    return res

# create weighting for word using letter frequency
def word_score_freq(word):
    return sum(letter_frequency[x] for x in word)


def get_guess(guess_wordList, sol_wordList):
    
    if len(sol_wordList) < 10:
        guess_wordList = sol_wordList    
    
    
    def evaluate_guess(word, wordList):
        result_strings: dict[str, int] = {}
        
        for solution in wordList:
            str = create_result(word, solution)
            result_strings[str] = result_strings.get(str, 0) + 1
        
        
        avg_size = sum((s * s for s in result_strings.values())) / sum((s for s in result_strings.values()))
        
        #calculate score of word
        return avg_size


    bestGuess = ""
    minScore = -1
    for word in guess_wordList:
        score = evaluate_guess(word, sol_wordList)
        if score < minScore or minScore == -1:
            minScore = score
            bestGuess = word
            
    # print(minScore, bestGuess)
    return bestGuess
    

'''
testing
'''

# best first guess is roate, try running get_guess with no previous knowledge

words_per_guess = {}

def eval(answer):
    num_guesses = 0
    currWords = guess_words
    possible_solutions = solution_words
    
    while True:
        num_guesses += 1
        if num_guesses == 1:
            word = "roate"
        else:
            word = get_guess(guess_words, possible_solutions)
        # print("guess:", word)
        
        result = create_result(word, answer)
        # print("result:", result)
        if result == "GGGGG":
            break
        
        currWords = updateWithGuess(currWords, word, result)
        possible_solutions = updateWithGuess(possible_solutions, word, result)
        # print("words left guess:", len(currWords), "solutions:", possible_solutions)
    
    print(answer, num_guesses)
    words_per_guess[num_guesses] = words_per_guess.get(num_guesses, 0) + 1
    

# for word in solution_words:
#     eval(word)
    # print("ANSWER:", word)

# print(words_per_guess)

# results: {3: 1157, 4: 915, 6: 22, 2: 74, 5: 140, 8: 2, 7: 5} which is the same as 3.5257019438444925

# results = {3: 1157, 4: 915, 6: 22, 2: 74, 5: 140, 8: 2, 7: 5}
# sum = 0
# total = 0

# for val in results:
#     sum += val * results[val]
#     total += results[val]

# print(sum/total)

def solve():
    num_guesses = 0
    currWords = guess_words
    possible_solutions = solution_words
    
    while True:
        num_guesses += 1
        if num_guesses == 1:
            word = "roate"
        else:
            word = get_guess(guess_words, possible_solutions)
        print("guess:", word)
        
        result = input("guess result: ")
        # print("result:", result)
        if result == "GGGGG":
            print("Yeet!")
            break
        
        currWords = updateWithGuess(currWords, word, result)
        possible_solutions = updateWithGuess(possible_solutions, word, result)
        # print("words left guess:", len(currWords), "solutions:", possible_solutions)

# solve()

def possibilities():
    possible_solutions = solution_words
    num_guesses = int(input("number of guesses: "))
    
    while num_guesses > 0:
        word = input("guess: ")
        result = input("result: ")
        
        possible_solutions = updateWithGuess(possible_solutions, word, result)
        print(len(possible_solutions), possible_solutions)
        
        num_guesses -= 1
        

possibilities()
    