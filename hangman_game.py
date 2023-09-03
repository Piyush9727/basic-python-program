import random
import string

def hangman_game():
    misteks=7
    low = 5
    up = 12
    length = random.randint(low, up)

    alphabet = string.ascii_lowercase
    random_word = ''.join(random.choice(alphabet) for _ in range(length))
    print(random_word)
    guessed_word = ["_"] * len(random_word)

    

    #for user_letter in alphabet:
    while misteks>0 and "_" in guessed_word:
        user_letter=input(f"Guess the letter = ")

        if len(user_letter)!=1:
            print("enter single letter only from alphabet ")
            continue
        if user_letter in random_word:
            for n in range(len(random_word)):
                if random_word[n] == user_letter:
                    guessed_word[n] = user_letter
                    print("Correct!!!")
                    

        
        else:
            print(f"{user_letter} is not in word so Try again")
            misteks-=1
            print(f"remaining chances => {misteks}")

        
    if misteks==0:
        print("your chances are over")
    
    if "_" not in guessed_word:
            print("You guessed correct word")
            print(" ".join(guessed_word))


hangman_game()

    

    


