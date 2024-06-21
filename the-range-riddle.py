# 1. The Range Riddle
# Objective: The aim of this assignment is to deepen your understanding of Python's range() function.

# Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", 
# "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood 
# from the list and print it. Ensure that your program includes the use of the random module to select the mood.

# Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."
import random

emotions = ["Happy", "Sad", "Excited", "Lethargic", "Scared", "Optimistic", "Tired", "Depressed", "Silly", "Playful"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#days at random
for day in range(len(days)):
    random_day = random.randint(0,len(days)-1)
    for emotion in range(len(emotions)):
        random_emotion = random.randint(0, len(emotions)-1)
    print("Today is " + days[random_day] + ", I'm feeling " + emotions[random_emotion])


print("-----------------------------------------------------------------------------------------------")

#days in order
for day in range(len(days)):
    #random_day = random.randint(0,len(days)-1)
    for emotion in range(len(emotions)):
        random_emotion = random.randint(0, len(emotions)-1)
    print("Today is " + days[day] + ", I'm feeling " + emotions[random_emotion])

