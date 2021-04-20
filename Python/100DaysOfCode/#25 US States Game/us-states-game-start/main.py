import turtle
import pandas

screen = turtle.Screen()
screen.title('The U.S. States')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states = data.state.tolist()
guessed = []
yup = 0
probs = len(data['state'])
game_over = False
writer = turtle.Turtle()
writer.ht()
writer.pu()

while not game_over:
    answer = screen.textinput(title=f"{yup}/{probs}!", prompt="Guess a state name?")
    if answer.title() == 'Quit':
        missing_states = [state for state in states if state not in guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('States_To_Learn.csv')
        exit()

    elif yup == 50:
        writer.goto(-250, 0)
        writer.write("Congratulations!", move=False, font=('Courier', 40, 'normal'))

    elif answer.title() in states and answer.title() not in guessed:
        state_info = data[data.state == answer.title()]
        writer.goto(int(state_info.x), int(state_info.y))
        writer.write(answer.title())
        yup += 1
        guessed.append(answer.title())


screen.exitonclick()
