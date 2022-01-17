import json, random

f = open('guess_dictionary.json')
guess_words = json.load(f)
f.close()

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

def play(answer):
    num_guesses = 0
    
    while True:
        num_guesses += 1
        word = input("guess: ")
        
        result = create_result(word, answer)
        print("result:", result)
        if result == "GGGGG":
            break
        
    
    print(num_guesses)



answer = random.choice(guess_words)

play(answer)