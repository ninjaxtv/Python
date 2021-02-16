print("Hello how are you!!!")
score = 0

# QUESTION 1
answer1 = input("What is the capitel of West bengal? \na. Lucknow \nb. kolkata \nc. Delhi \nAnswer:  ")
if answer1 == "b" or answer1 == "kolkata":
    score += 1
    print("Correct!!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!!!")
    print("Score: ", score)
    print("\n")


# QUESTION 2
answer2 = input("Who is priminister of India? \na. Pm narendra Modi \nb. Jawaharlal nehru \nc. Lal bahadur shastri \nAnswer:  ")
if answer2 == "a" or answer2 == "Pm narendra Modi":
    score += 1
    print("Correct!!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!!!")
    print("Score: ", score)
    print("\n")


# QUESTION 3
answer3 = input("When is holi held? \na. Jan \nb. March \nc. April \nAnswer:  ")
if answer3 == "b" or answer3 == "March":
    score += 1
    print("Correct!!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!!!")
    print("Score: ", score)
    print("\n")

# QUESTION 4
answer4 = input("Name th monument in India built by shah jhah? \na. Golden temple \nb. qutub Minar \nc. Taj mahal \nAnswer:  ")
if answer4 == "c" or answer4 == "Taj mahal":
    score += 1
    print("Correct!!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!!!")
    print("Score: ", score)
    print("\n")
# QUESTION 5
answer5 = input("Name richest man in the world? \na. Golden temple \nb. Bill gates \nc. Jef Bezoz \nAnswer:  ")
if answer5 == "c" or answer5 == "Jef Bezoz":
    score += 1
    print("Correct!!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!!!")
    print("Score: ", score)
    print("\n")



#FINAL MESSAGE
if score <= 1:
    print("Your final score is:", score, "- You are bad!!!")
elif score == 2:
    print("Your total score is:", score, "- You went Ok.")
elif score == 3:
    print("Your total score is:", score, "- You are good")
elif score == 4:
    print("Your total score is:", score, "-You are very good")
else:
    print("Your total score is:", score, "-You are quiz master")




    
