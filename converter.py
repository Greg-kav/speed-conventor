import turtle
import tkinter as tk

window = turtle.Screen()
window.title("converter")
window.bgcolor("black")

instractions1=turtle.Turtle()
instractions1.hideturtle()
instractions1.hideturtle()
instractions1.color("blue")
instractions1.penup()
instractions1.goto(0,300)
instractions1.write("Convert m/s to km/h", align="center", font=("Arial", 24, "normal"))

answear1=turtle.Turtle()
answear1.hideturtle()
answear1.hideturtle()
answear1.color("red")
answear1.penup()
answear1.goto(0,200)
answear1.write("Convert m/s to km/h", align="center", font=("Arial", 24, "normal"))

instractions2=turtle.Turtle()
instractions2.hideturtle()
instractions2.hideturtle()
instractions2.color("blue")
instractions2.penup()
instractions2.goto(0,50)
instractions2.write("Convert km/h to m/s", align="center", font=("Arial", 24, "normal"))

answear2=turtle.Turtle()
answear2.hideturtle()
answear2.hideturtle()
answear2.color("red")
answear2.penup()
answear2.goto(0,-50)
answear2.write("Convert m/s to km/h", align="center", font=("Arial", 24, "normal"))

def submit_input():
    user_input = entry.get()
    instractions1.clear()
    instractions1.write(f"User input: {user_input} m/s", align="center", font=("Arial", 24, "normal"))
    x = float(user_input)
    x = (x * 0.001)*3600
    answear1.clear()
    answear1.write(f"The {user_input} m/s is {x} Km/h", align="center", font=("Arial", 24, "normal"))

def submit_input2():
    user_input2 = entry2.get()
    instractions2.clear()
    instractions2.write(f"User input: {user_input2} Km/h", align="center", font=("Arial", 24, "normal"))
    y = float(user_input2) #metatrepei to text se dekadiko
    y =( y * 1000)/3600
    answear2.clear()
    answear2.write(f"The {user_input2} Km/h is {y} m/s", align="center", font=("Arial", 24, "normal"))

root = window._root 

label = tk.Label(root, text="Enter speed in m/s:", font=("Arial", 16))
label.pack()

entry = tk.Entry(root)
entry.pack() 

submit_button = tk.Button(root, text="Convert", command=submit_input)
submit_button.pack()

label2 = tk.Label(root, text="Enter speed in km/h:", font=("Arial", 16))
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

submit_button2 = tk.Button(root, text="Convert", command=submit_input2)
submit_button2.pack()

window.mainloop()