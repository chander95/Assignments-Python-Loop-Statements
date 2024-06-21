# 2. Double Scoop with Nested Loops
# Objective: The aim of this assignment is to practice using nested loops in Python.

# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
# for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate 
# over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly 
# select the mood.

# Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were 
# tired"


import random

emotions = ["Happy", "Sad", "Excited", "Lethargic", "Scared", "Optimistic", "Tired", "Depressed", "Silly", "Playful"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["morning", "afternoon", "evening"]

for day in range(len(days)):
    #random_day = random.randint(0,len(days)-1)
    for time in range(len(time_of_day)):
        random_time = random.randint(0,len(time_of_day)-1)
        for emotion in range(len(emotions)):
            random_emotion = random.randint(0, len(emotions)-1)
    print("On " + days[day] + " " + time_of_day[random_time] + " I was feeling " + emotions[random_emotion])
