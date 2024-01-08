import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess Indian States")
image="India-state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_states= []

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States correct",
                                    prompt="What's another state name").title()
    if answer_state =="exit":
        missing_state=[]
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_states.csv")

    break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)



    # answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States correct", prompt="What's another state name")


screen.exitonclick()