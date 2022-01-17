import json, random

f = open('guess_dictionary.json')
guess_words = set(json.load(f))
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

# yes or no outline
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

def play():
    answer = random.choice(guess_words)
    
    num_guesses = 0
    
    while True:
        num_guesses += 1
        word = input("guess: ")
        while(len(word) != 5):
            word = input("guess should be 5 letters: ")
        while(word not in guess_words):
            word = input("not a valid word, new guess: ")
        
        result = create_result(word, answer)
        print("result:", result)
        if result == "GGGGG":
            break
        
    
    print(num_guesses)

    if(yes_or_no("want to play again?")):
        play()
    else:
        return


play()