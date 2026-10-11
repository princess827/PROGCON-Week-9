rainbowColor = [""] * (7)
userGuesses = [""] * (7)

rainbowColor[0] = "red"
rainbowColor[1] = "orange"
rainbowColor[2] = "yellow"
rainbowColor[3] = "green"
rainbowColor[4] = "blue"
rainbowColor[5] = "indigo"
rainbowColor[6] = "violet"
for i in range(0, 6 + 1, 1):
    print("Enter the colors of the rainbow " + str(i + 1) + ":")
    userGuesses[i] = input()
    correctCount = 0
for i in range(0, 6 + 1, 1):
    if userGuesses[i] == rainbowColor[i]:
        correctCount = correctCount + 1
print("You got " + str(correctCount) + " correct answers.")
if correctCount >= 6:
    print("Grade: excellent")
else:
    if correctCount >= 3:
        print("Grade: average")
    else:
        print("Grade: poor")
