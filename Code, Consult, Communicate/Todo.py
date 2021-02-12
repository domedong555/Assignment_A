# Let’s start with the good-old trusty todo list, the “Hello, World” of full programs. You’re going to write a command-line todo list program that meets the following specifications:

# Prompt the user to enter a chore or task. Store the task in a permanent location so that the task persists when the program is restarted.
# Allow the user to enter as many tasks as desired but stop entering tasks by entering a blank task. Do not store the blank task.
# Display all the tasks.
# Allow the user to remove a task, to signify it’s been completed.
# Persist todos to Redis
# Easy

import redis
todoRef = redis.Redis()

def todoList():
    todoRef = redis.Redis()
    state = True

    while state==True :
        task = []
        try: 
            task_File = open('todoList.txt', 'r')
            task_Data = task_File.read().splitlines()
            task_File.close()
        except FileNotFoundError:
            task_File = open('todoList.txt', 'w+')
            task_Data = task_File.read().splitlines()
            task_File.close()

        selected_choice = input("TODO LIST \nType 'Task' to add todo task to program. \nType 'View' to display all task. \nType 'Delete' to remove task.\nType 'Exit' to exit the program.\n")

        while selected_choice=='Task':
            task_add = input("Type task to add  or press enter to leave.\n")
            if task_add=="":
                break
            else:
                task.append(task_add)
                task_File = open('todoList.txt', 'a')
                n = 1
                for i in task:
                    j = str(i)
                    print(" - ",j)
                    task_File.write(j+"\n")
                    todoRef.sadd("todo_task",j)
                task_File.close()
                break
        while selected_choice=='Delete':
            task_File = open('todoList.txt', 'r')
            task_Data = task_File.read().splitlines()
            task_File.close()
            task_File = open('todoList.txt', 'w+')
            print(task_Data)
            typed = input("Type a task that you want to remove or press enter to leave.\n")
            if typed=="":
                break
            elif (typed in task_Data) == True:
                todoRef.srem("todo_task",typed)
                task_Data.remove(typed)
                for i in task_Data:
                    task_File.write(i+"\n")
                break
            else:
                print("This task do not exist.\n")
            task_File.close()
        while selected_choice=='View':
            if len(task_Data)==0:
                print("There are no tasks at this time.")
            else:
                print("TODO LIST\n")
                n = 1
                for i in task_Data:
                    print(n," ",i)
                    n += 1
            break
        if selected_choice=='Exit':
            state = False

todoList()