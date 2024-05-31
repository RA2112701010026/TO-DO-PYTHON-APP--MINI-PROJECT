def task():
    tasks = [] 
    print("WELCOME TO TASK MANAGEMENT APP.........!")

    total_tasks = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name) 

    print(f"Today's tasks are:\n{tasks}")
    while True:
        operation = int(input("Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\n"))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)  
            print(f"Task '{add}' has been successfully added.")
        elif operation == 2:
            update = input("Enter the task name you want to edit: ")
            if update in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(update)
                tasks[ind] = up  
                print(f"Updated task: '{update}' to '{up}'.")
            else:
                print(f"Task '{update}' not found.")  
        elif operation == 3:
            delete = input("Enter the task you want to delete: ")
            if delete in tasks:
                tasks.remove(delete) 
                print(f"Task '{delete}' has been deleted.")
            else:
                print(f"Task '{delete}' not found.") 
        elif operation == 4:
            print(f"Total tasks are: {tasks}")
        elif operation == 5:
            print("Closing the program.......!")
            break
        else:
            print("Select a valid option.")

# Run the task management program
task()
