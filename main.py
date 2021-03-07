# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random

x = 0
type_speed = 0
type_time = 0


def speed_test():
    """A function that displays a random sentence to test a user's typing speed"""

    global x, type_time, type_speed

    type_speed = 0
    type_time = 0

    # loop for destroying the window after a test
    if x == 0:
        window.destroy()
        x += 1

    def calculate():
        """A function that calculates a user's typing speed"""

        global type_time, type_speed

        # end the timer when the new window is destroyed
        end_time = timer()

        # converting the user's input into a list of words
        word_list = text_box.get("1.0", END).split()

        # calculate time and speed
        type_time = round(end_time - start_time, 2)
        type_speed = round((len(word_list) / type_time) * 60)

        x4.config(text=f"Time: {type_time} seconds\nSpeed: {type_speed} wpm")

    sentences = ['"The way to get started is to quit talking and begin doing"',
                 '"If life were predictable it would cease to be life, and be without flavor"',
                 '"Life is what happens when you are busy making other plans"',
                 '"When you reach the end time of your rope, tie a knot in it and hang on"',
                 '"Always remember that you are absolutely unique. Just like everyone else"',
                 '"The future belongs to those who believe in the beauty of their dreams"',
                 '"It is during our darkest moments that we must focus to see the light"']

    # select a random sentence for testing the speed of a user
    sentence = random.randint(0, (len(sentences) - 1))

    # start the timer when the new window is opened
    start_time = timer()
    windows = Tk()
    windows.minsize(width=600, height=300)
    windows.title("Typing Speed Test")

    # use label method of tkinter for labeling in windows
    x2 = Label(windows, text=sentences[sentence], font=("Arial", 10, "bold"))
    x2.pack(pady=10)

    x3 = Label(windows, text="Type the sentence above as fast as you can", font=("Arial", 10, "bold"))
    x3.pack(pady=10)

    # Text box
    text_box = Text(windows, width=50, height=5)
    text_box.pack(pady=10)

    x4 = Label(windows, text=f"Time: {type_time} seconds\nSpeed: {type_speed} wpm", font="times 20")
    x4.pack(pady=10)

    # buttons to submit output and calculate type speed
    b2 = Button(windows, text="Done", command=calculate, width=12, bg="green")
    b2.pack(pady=10)

    b3 = Button(windows, text="Try Again", command=speed_test, width=12, bg="grey")
    b3.pack(pady=10)
    windows.mainloop()


# creating window using gui
window = Tk()

# the size of the window is defined
window.minsize(width=450, height=200)
window.config(padx=40, pady=20)
window.title("Typing Speed Test")

x1 = Label(text="Check how fast you type", font=("Arial", 10, "bold"))
x1.pack(pady=20)

b1 = Button(text="Start", command=speed_test, width=12, bg="skyblue")
b1.pack()

window.mainloop()
