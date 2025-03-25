name = input('Type your name: ')
print("Welcome", name, "to this adventure!")

answer = input("You are on cave with two option, choose left or right? ")

if answer == 'left':
    answer = input("The cave become much darker there and some monsters showup, You have to fight or run? ")
    if answer == "fight":
        print("You fight till end and the monster gave up, the great door behind the monster opens and you get out of the cave, You won")
    else:
        print("You run till you are out fuel then the monster ate you, you lost!")
elif answer == 'right':
    print('You lose because this is not the right path, you lost!')