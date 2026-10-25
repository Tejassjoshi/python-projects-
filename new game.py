import random as r
guess_num = r.randint(1,100)
point = 1
num = 0
print("Guess the number from 1 to 100 game")
take_name = input("Enter your name ")

while num != guess_num :
    if(take_name == "Tejas"):
           print(guess_num)

    num = int(input("Guess the number "))

    if(num > guess_num):
            print("Try lower")
            point +=1

    if(num < guess_num):
                print("Try higher")
                point +=1

    if(num == guess_num):
        break
        
print(f"congratulations {take_name} You guessed in attempts: ",point)