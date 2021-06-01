import turtle
import pandas

theScreen = turtle.Screen()
theScreen.title("U.S States Game")
theImage = "blank_states_img.gif"
theScreen.addshape(theImage)
turtle.shape(theImage)
guessedStates = []

while len(guessedStates) < 50:
    guessState = str.title(theScreen.textinput(title=f"{len(guessedStates)}/50 States Correct", prompt="What's "
                                                                                                       "another "
                                                                                                       "state's "
                                                                                                       "name?"))
    data = pandas.read_csv("50_states.csv")
    theStates = data.state.to_list()

    if guessState == "Exit":
        missedStates = [state for state in theStates if (state not in guessedStates)]
        newData = pandas.DataFrame(missedStates)
        newData.to_csv("statesToLearn.csv")
        break

    if guessState in theStates:
        if guessState in guessedStates:
            pass

        else:
            guessedStates.append(guessState)
            theTurtle = turtle.Turtle()
            theTurtle.penup()
            theTurtle.hideturtle()
            theStateData = data[data.state == guessState]
            theTurtle.goto(int(theStateData.x), int(theStateData.y))
            # theTurtle.write(theStateData.state.item())
            theTurtle.write(guessState)
