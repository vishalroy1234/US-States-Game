
import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.Turtle("blank_states_img.gif")


guessed_states = []
while len(guessed_states) < 50:
    input_state = screen.textinput(f"U.S. States Game  Score:{len(guessed_states)}/50", "Enter a state name.").title()
    user_state = data[data.state == input_state]
    if input_state == 'Exit':
        break
    elif user_state.size == 0:
        pass
    else:
        guessed_states.append(user_state.state.item())
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(float(user_state.x), float(user_state.y))
        tim.write(user_state.state.item())

states_to_learn = [state for state in data['state'].to_list() if state not in guessed_states]
pandas.DataFrame(states_to_learn, columns=['States to remember']).to_csv('states_to_learn.csv')




