# Treasure map game

#create 3x3 game map
from re import X

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (Ex. column=2, row=3 as 23)")

if int(position[0]) > 3 or int(position[0]) < 1:
    print("Error. Enter a number between 1 and 3 for the row and column.")
elif int(position[1]) > 3 or int(position[1]) < 1:
    print("Error. Enter a number between 1 and 3 for the row and column.")
else:
    #Process user coordinates
    column = int(position[0]) #2
    row = int(position[1]) #3
    column_index = column-1 #1
    row_index = row-1 #2

    print(f"You chose column {column}, which is index {column_index}")
    print(f"You chose row {row}, which is index {row_index}")

    #update map
    map[row_index][column_index] = "X"


    #print updated map with treasure location
    print(f"{row1}\n{row2}\n{row3}")