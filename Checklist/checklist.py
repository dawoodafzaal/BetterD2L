checkList = []

def addToList():
    listItem = input("Add something to the checklist: ")
    if listItem == "":
        return
    else:
        checkList.append(listItem)

def removeFromList():
    removeItem = input("Remove something from the checklist by number: ")
    if removeItem == "":
        return
    else:
        if len(checkList) < int(removeItem):
            print("Can't remove an item that doesn't exist!")
            return
        del checkList[int(removeItem)-1]

def displayList(counter):
    if len(checkList) == 0:
        print("List is empty!")

    for item in checkList:
        counter += 1
        print("#", counter," ", item)

def main():
    counter = 0
    while 1:
        menu = input("1 to add, 2 to remove, 3 to view, 4 to quit: ")
        if menu == "1":
            addToList()
            displayList(counter)
        elif menu == "2":
            removeFromList()
            displayList(counter)
        elif menu == "3":
            displayList(counter)
        else:
            break

main()
