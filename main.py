import pandas
import turtle



screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "usQuiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("usQuiz/50_states.csv")
states_guessed = []
states = data.state.to_list()

while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        sng = [state for state in states if state not in states_guessed]
        new_data = pandas.DataFrame(sng)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        states_guessed.append(answer_state)
        t_state = turtle.Turtle()
        t_state.hideturtle()
        t_state.penup()
        state_data = data[data.state == answer_state]
        t_state.goto(int(state_data.x), int(state_data.y))
        t_state.write(answer_state)




screen.exitonclick()



