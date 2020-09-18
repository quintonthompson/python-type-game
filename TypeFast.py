import matplotlib.pyplot as plt
import time as t
mistakes = 0
playing = False
correct = False
gameRound = 0
wordAnswer = "HelloWorld"
correctTimes = {}

while(not playing):
    print('The goal is to type a give word as fast as you can 5 '\
    'times. The time it takes for you to type the word each time '\
    'is recorded and will display on a chart ')
    play = input("Are you ready to play? (press y)")
    if play == "y":
        playing = True
        while(gameRound < 5):
            print("back to the top")
            startTime = t.time()
            while(not correct):
                word = input("Type the word: HelloWorld  ")
                if(word != wordAnswer):
                    print("Incorrect")
                    mistakes = mistakes + 1
                    continue
                else:
                    print("Correct!")
                    correct = True

            timeToAnswer = t.time() - startTime
            gameRound = gameRound + 1
            correctTimes[gameRound] = round(timeToAnswer,2)
            correct = False
        print("The game is now over. You completed the game with " + str(mistakes) + " mistakes")
        keys = correctTimes.keys()
        values = correctTimes.values()
        plt.xticks(list(keys))
        plt.xlabel('Rounds')
        plt.ylabel('Time in Seconds')
        plt.bar(keys,values)
        plt.show()
    else:
        continue