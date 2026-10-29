calories_burned_min = 3.6 
current_min = 5


while current_min <= 30:
    calories_burned = calories_burned_min * current_min
    print(f"Calories burned a minute: {calories_burned:.2f}|",f"Minute: {current_min:.2f}")
    current_min += 5
