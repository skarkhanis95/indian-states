import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=953)
screen.title("India States & UTs Game")
image = "india-outline-map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("indian_states.csv")
all_states = data.state.to_list()
correct_count = 0
guesses_states = []
game_is_on = True
while game_is_on:
    if correct_count == len(all_states):
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(0,0)
        writer.write("YOU WON! You Got it ALL!!", move=False, align='Center', font=("Arial", 25, "bold"))
        game_is_on = False
    else:
        title = f"Correctly Guessed {correct_count}/{len(all_states)}"
        answer_state = screen.textinput(title=title, prompt="Enter Next State or UT Name").lower()
        if answer_state == "exit":
            break
        matched_state = data[data.state.str.lower() == answer_state]
        if not matched_state.empty:
            guesses_states.append(answer_state.title())
            new_pos = (int(matched_state.x), int(matched_state.y))
            writer = turtle.Turtle()
            writer.hideturtle()
            writer.penup()
            writer.goto(new_pos)
            writer.write(answer_state.title(),move=False, align='Center',font=("Arial",10,"bold"))
            correct_count += 1

# Creat CSV file of Missed States

missed_states = []
for state in all_states:
    if not state in guesses_states:
        missed_states.append(state)

missed_states_dict = {
    "Missed States": missed_states
}
df = pandas.DataFrame(missed_states_dict)
df.to_csv("Missed_States.csv")