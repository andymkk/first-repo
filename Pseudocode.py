START PROGRAM

goals = []

WHILE True:
PRINT "What do you want to do?"
PRINT "1. Make new goal"
PRINT "2. Add money to goal"
PRINT "3. See my goals"
PRINT "4. Check for reminders"
PRINT "5. Quit"

choice = INPUT "Enter number: "
IF choice == "1":
PRINT "Making new goal."
name = INPUT "Goal name: "
target = INPUT "How much money needed: "
date = INPUT "When needed (MM/DD/YYYY): "

new_goal = [name, float(target), date, 0.0, "Active"]
goals.append(new_goal)
PRINT "Goal made!"

ELSE IF choice == "2":
if goals is empty:
PRINT "No goals yet! Make one first."
ELSE:
PRINT "Your goals:
FOR i FROM 0 TO len(goals)-1:
PRINT str(i+1) + ". " + goals[i][0]

which = INPUT "Which goal number? "
money = INPUT "How much to add? "
goals[which-1][3] = goals[which-1][3] + float(money)
IF goals[which-1][3] >= goals[which-1][1]:
goals[which-1][4] = "Completed"
PRINT "CONGRATS! Goal reached!

ELSE:
PRINT "Money added! Keep saving."
ELSE IF choice == "3":
IF goals is empty:
PRINT "No goals yet."

ELSE:
PRINT "MY GOALS:
FOR goal IN goals:
PRINT "Goal: " + goal[0]
PRINT "Saved: $" + str(goal[3]) + " / $" + str(goal[1])
percent = (goal[3] / goal[1]) * 100
PRINT "Progress: " + str(percent) + "%"
PRINT "Status: " + goal[4]
PRINT "---"

ELSE IF choice == "4":
PRINT "Checking goals."
today = CURRENT DATE
FOR goal IN goals:
IF goal[4] == "Active":
days_left = CALCULATE days between today and goal[2]
# If due soon and not enough money
IF days_left =< 7 AND goal[3] < goal[1]:
needed = goal[1] - goal[3]
PRINT "ALERT: " + goal[0] + " needs $" + str(needed) + " in " + str(days_left) + " days!"

ELSE IF choice == "5":
PRINT "Goodbye!"

BREAK
ELSE:

PRINT "Please enter 1-5"
END WHILE

END PROGRAM

 