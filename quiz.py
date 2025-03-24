print("Welcome to my quiz!")
playing = input("Do you want to play? ")

if playing != 'yes':
    quit()

print("okay! lets play :)")

answer = input("What is Angular? ")
if answer == "Javascript Framework":
    print("Correct!")
else:
    print("Incorrect!")