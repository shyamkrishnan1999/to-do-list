
#function to add a task to our to-do-list
def addTask():
    fptr=open("To-do-list.txt","a")
    task=input("Enter Task:")
    fptr.writelines(task+"\n")
    print("Task added.")
    fptr.close()

#function to display our tasks
def displayTask():
    fptr=open("To-do-list.txt","r")
    tasks=fptr.readlines()
    fptr.close()
    for i in tasks:
        print(i)

    
#function to delete a task
def deleteTask():
    fptr=open("To-do-list.txt","r")
    tasks=fptr.readlines()
    fptr.close()
    
    deltask=input("Enter the task to be deleted:")

    try:
        tasks.remove(deltask)
    except ValueError:
        print("No Such Task Found")

    fptr=open("To-do-list.txt","w")
    fptr.writelines(tasks)
    print("Task deleted.")
    fptr.close()


#main code

flg=True

#Menu
print("To-do-list")
print("1.Add a task\n2.Display tasks\n3.Delete a task\n4.Exit")

while(flg):

    choice=int(input("Enter your choice(1-4):"))
    choices={1:addTask,2:displayTask,3:deleteTask,4:exit}
    call=choices.get(choice,"wrong")


    if call=="wrong":
        print("No such choice")
    else:
        call()

    cont=input("Do you want to continue:")

    if(cont.upper()=="N" or cont.lower()=="no"):
        flg=False


