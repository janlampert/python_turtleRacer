import turtle
import random
import time

turtle.hideturtle()
turtle.bgcolor("lightblue")

def user_input():
    print ("--Welcome to turtle Racer!--")
    print("-Turtle list-\n1: Red\n2: Blue\n3: Green\n4: Pink\n5: Purple")
    turtle_bet = input ("On which turtle do you guess? (1-5) ")

    if turtle_bet.isdigit() and int(turtle_bet) <= 5 and int(turtle_bet) >= 1:
        print (f"Bet on turtle {turtle_bet} succesfully placed! ")
        return True, turtle_bet

    else:
        print ("Please enter a number between 1-5.")
        quit()

def turtle_race(turtle_bet):
    run=True

    num1 = turtle.Turtle()
    num1.color("red")
    num1.shape("turtle")
    num1.left(90)
    num1.penup()
    num1.backward(300)
    num1.left(90)
    num1.forward(270)
    num1.right(90)
    num1.pendown()

    num2 = turtle.Turtle()
    num2.color("blue")
    num2.shape("turtle")
    num2.left(90)
    num2.penup()
    num2.backward(300)
    num2.left(90)
    num2.forward(135)
    num2.right(90)
    num2.pendown()

    num3 = turtle.Turtle()
    num3.color("green")
    num3.shape("turtle")
    num3.left(90)
    num3.penup()
    num3.backward(300)
    num3.pendown()

    num4 = turtle.Turtle()
    num4.color("pink")
    num4.shape("turtle")
    num4.left(90)
    num4.penup()
    num4.backward(300)
    num4.right(90)
    num4.forward(135)
    num4.left(90)
    num4.pendown()

    num5 = turtle.Turtle()
    num5.color("purple")
    num5.shape("turtle")
    num5.left(90)
    num5.penup()
    num5.backward(300)
    num5.right(90)
    num5.forward(270)
    num5.left(90)
    num5.pendown()

    finish = turtle.Turtle()
    finish.color("black")
    finish.shape("circle")
    finish.left(90)
    finish.penup()
    finish.forward(300)
    finish.left(90)
    finish.pendown()
    finish.forward(400)
    finish.left(180)
    finish.forward(800)
    finish.hideturtle()

    print (3)
    time.sleep(1)
    print (2)
    time.sleep(1)
    print (1)
    time.sleep(1)
    print ("GO!")

    while run:
        
        num1.forward(random.randint(1, 5))
        num2.forward(random.randint(1, 5))
        num3.forward(random.randint(1, 5))
        num4.forward(random.randint(1, 5))
        num5.forward(random.randint(1, 5))

        if num1.pos()[1] == 300.00000000000006 or num1.pos()[1] == 301.00000000000006 or num1.pos()[1] == 302.00000000000006 or num1.pos()[1] == 303.00000000000006 or num1.pos()[1] == 304.00000000000006 or num1.pos()[1] == 305.00000000000006:
            run=False
            print ("Race Finished!")
            print ("Number 1 (Red) won!\n")
            if int(turtle_bet) == 1:
                print ("Your turtle won! Congratulations!")
            else:
                print ("You lost.")

        elif num2.pos()[1] == 300.0 or num2.pos()[1] == 301.0 or num2.pos()[1] == 302.0 or num2.pos()[1] == 303.0 or num2.pos()[1] == 304.0 or num2.pos()[1] == 305.0:
            
            run=False
            print ("Race Finished!")
            print ("Number 2 (Blue) won!\n")
            if int(turtle_bet) == 2:
                print ("Your turtle won! Congratulations!")
            else:
                print ("You lost.")
        elif num3.pos()[1] == 300.0 or num3.pos()[1] == 301.0 or num3.pos()[1] == 302.0 or num3.pos()[1] == 303.0 or num3.pos()[1] == 304.0 or num3.pos()[1] == 305.0:
            run=False
            print ("Race Finished!")
            print ("Number 3 (Green) won!\n")
            if int(turtle_bet) == 3:
                print ("Your turtle won! Congratulations!")
            else:
                print ("You lost.")

        elif num4.pos()[1] == 300.0 or num4.pos()[1] == 301.0 or num4.pos()[1] == 302.0 or num4.pos()[1] == 303.0 or num4.pos()[1] == 304.0 or num4.pos()[1] == 305.0:
            run=False
            print ("Race Finished!")
            print ("Number 4 (Pink) won!\n")
            if int(turtle_bet) == 4:
                print ("Your turtle won! Congratulations!")
            else:
                print ("You lost.")

        elif num5.pos()[1] == 300.0 or num5.pos()[1] == 301.0 or num5.pos()[1] == 302.0 or num5.pos()[1] == 303.0 or num5.pos()[1] == 304.0 or num5.pos()[1] == 305.0:
            run=False
            print ("Race Finished!")
            print ("Number 5 (Purple) won!\n")
            if int(turtle_bet) == 5:
                print ("Your turtle won! Congratulations!")
            else:
                print ("You lost.")


def game():
    user = user_input()
    status = user[0]
    turtle_bet = user[1]
    
    

    if status:
        
        turtle_race(turtle_bet)
        
    else:
        print ("An error occured.") 

    print ("I hope you had a great time!- Jan")
    

game()

turtle.getscreen()._root.mainloop()
