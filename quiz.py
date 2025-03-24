print("Welcome to my quiz!")
playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("okay! lets play :)")
score = 0

# Question 1
answer = input("What is Angular? ")
if answer.lower() == "javascript framework":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What is MVC Stand for? ")
if answer.lower() == "model view controller":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What is DI means? ")
if answer.lower() == "dependency injection":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("Which is the latest Angular version? ")
if answer.lower() == "19":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 5
answer = input("What is Angular CLI? ")
if answer.lower() == "angular command line interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got "+ str(score) + " question correct!")