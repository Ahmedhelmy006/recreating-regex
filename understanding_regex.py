import sys, re

#pattern = r"^(.)(.)(.).?\3\2\1$"
pattern = r"(.)"
input("Hello. Today you'll be learning regex! Excited? \n")
print("Whatever, Let's begin. This is the first example: \n")
score = 0
print(pattern)

print("\nYour if your next input matches the pattern, it will print True. and you will get a score of 1. " \
      "\nIf it doesn't, it will print False and your score will be deducted one from it. If you get 5 you win, if you get -5 you lose! " \
      "\nBe a good boy and win!\n")

while True:
    user_input = input("What's your answer?")
    if user_input == "\q":
        break
    if score == 5:
        print("Goodboy! You win")
        break
    if score == -5:
        print("Not a very good boy apparently...")
        break
    else:
        if re.match(pattern=pattern, string=user_input):
            print(True)
            score +=1 
            print(f"Your score is {score}")
            continue

        if not re.match(pattern=pattern, string=user_input):
            print(False)
            score -=1
            print(f"Your score is {score}")
            continue