todo = open("stored/todo.txt").read().split("\n")
todone = open("stored/todnoe.txt").read().split("\n")
h, b = 0, 0
print("Actions:\nv - views your current to-do list\nc - views your completed to-do list\ncc - clear your completed to-do list\nn - adds a new to-do entry\nr - prints the current to-do list and prompts you to move one to the completed one\ne - stops program and exits window\n")
while True:
    x = input("Action: ").lower()
    if x == "v": # view
        for i in range(len(todo)):
            print(str(i + 1) + ": " + todo[i])
        print()
    elif x == "c": # view completed
        for i in range(len(todone)):
            print(str(i + 1) + ": " + todone[i])
        print()
    elif x == "n": # add entry
        h = input("What would you like to add to your to-do list? ")
        todo.append(h)
    elif x == "r": # complete
        for i in range(len(todo)):
            print(str(i + 1) + ": " + todo[i])
        print()
        m, h = input("Which one do you want to mark as complete (Type the number, press 'c' to cancel)? "), 0
        while h == 0:
            try:
                if m == "c":
                    h += 1
                else:
                    out = int(m) - 1
                    h += 1
            except:
                m = input("Bad input, try again: ")
                print(out)
        if m != "c":
            todone.append(todo[out])
            todo.pop(out)
    elif x == "cc":
        if input("Are you COMPLETELY SURE you want to PERMENANTLY DELETE your completed todo list?\nIf so, type \"YES\" in all caps.\n") == "YES":
            todone = ""
            print("You're To-done list has been cleared.")
    elif x == "e": # end
        b = 1
    else:
        print("Bad input\n")
    td = ""
    tde = ""
    randomVar = 0
    for i in range(len(todo)):
        if randomVar == 0:
            td = todo[i]
            randomVar += 1
        else:
            td += "\n"
            td += todo[i]
    randomVar = 0
    for i in range(len(todone)):
        if randomVar == 0:
            tde = todone[i]
            randomVar += 1
        else:
            tde += "\n"
            tde += todone[i]
    todotxt = open("stored/todo.txt", "w")
    todonetxt = open("stored/todnoe.txt", "w")
    todotxt.write(td)
    todonetxt.write(tde)
    todotxt.close()
    todonetxt.close()
    if b == 1:
        print("Thank you for using this program. See you soon!")
        from time import sleep as die
        die(2)
        break