import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S STATE GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_state = []
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
while len(guessed_state) < 50:
    answerstate = screen.textinput(title=f"{len(guessed_state)}/50 states guessed",
                                   prompt="What's the another state name.").title()
    if answerstate == "Exit":
        missing_list = []
        for state in states:
            if state not in guessed_state:
                missing_list.append(state)
        new_data = pd.DataFrame(missing_list)
        new_data.to_csv("States to learn")
        print(missing_list)
        break
    if answerstate in states:
        guessed_state.append(answerstate)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answerstate]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answerstate)
