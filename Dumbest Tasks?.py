'''Task 1: Printing a string'''
print("Jello World!")

'''Task 2: Calendrics'''
def weekday(day1_weekday, day1, day2):
    
    if day1_weekday == "Sunday":
        day1_weekday = 1
    if day1_weekday == "Monday":
        day1_weekday = 2
    if day1_weekday == "Tuesday":
        day1_weekday = 3
    if day1_weekday == "Wednesday":
        day1_weekday = 4
    if day1_weekday == "Thursday":
        day1_weekday = 5
    if day1_weekday == "Friday":
        day1_weekday = 6
    if day1_weekday == "Saturday":
        day1_weekday = 7
        
    days_difference = day2 - day1
    
    day2_weekday = (day1_weekday + days_difference - 1) % 7 + 1

    if day2_weekday == 1:
        print("Sunday")
    if day2_weekday == 2:
        print("Monday")
    if day2_weekday == 3:
        print("Tuesday")
    if day2_weekday == 4:
        print("Wednesday")
    if day2_weekday == 5:
        print("Thursday")
    if day2_weekday == 6:
        print("Friday")
    if day2_weekday == 7:
        print("Saturday")

#Tests
weekday("Thursday", 3, 4)
weekday("Thursday", 3, 116)
weekday("Friday", 116, 3)
