# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_cords = turtle.Turtle()
state_cords.hideturtle()
state_cords.penup()
wrong = turtle.Turtle()
wrong.hideturtle()
wrong.penup()
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

x_cor = data.x.to_list()
y_cor = data.y.to_list()
guessed_states = []
wrong_guesses = 0
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} states correct", prompt="Name a state").title()

    if answer_state == "Exit":
        missed_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        cord_num = states_list.index(answer_state)
        state_cords.goto(x_cor[cord_num], y_cor[cord_num])
        state_cords.write(answer_state)

    else:

        wrong.clear()
        wrong_guesses += 1
        wrong.goto(0, 250)
        wrong.write(f"Wrong Guesses: {wrong_guesses}")
