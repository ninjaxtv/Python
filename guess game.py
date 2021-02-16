print("Can you guess it game!!!")
print("Who was founder of microsoft??")

secret_word = "Bill gates"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of chances You lose!")
else:
    print("You win!!!")

print("which programming language is roblox made in??")

secret_word2 = "Lua"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word2 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of chances You lose!")
else:
    print("You win!!!")

print("who is current CEO of microsoft??")

secret_word3 = "Satya naddela"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word3 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of chances You lose!")
else:
    print("You win!!!")
    



    
