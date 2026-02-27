import models , services , storage

service = services.ToDoService()
#==================================================================================================================================================

def add_task():
    list_tasks()
    print("=======================================================================================")
    while True:
        title = input("enter task title : ")
        if title.strip() == "":
            print("empty input is not allowed...try again")
        else:
            break
    description = input("enter task description : ")
    try :
        print(f"current range of priorities is from 1 to {len(storage.load_tasks())+1} , you can enter any number in this range to set the priority of your task")
        priority = int(input("enter task priority to change the pririties of other tasks ( 0 will top of list and -1 goes to buttom of list ): "))
    except ValueError:
        print("invalid input for priority")
    print("=======================================================================================")
    error = service.add_task(title,description,priority)
    if not error:
        print("Invalid priority input, task will be added to the end of the list.change it in the change task info menu if you want to change it.")
    else:
        print(f"task with '{title}' title added successfully.")

#==================================================================================================================================================

def remove_task():
    list_tasks()
    print("=======================================================================================")
    try:
        tasks = service.list_tasks()
        priority = int(input("enter the priority of task you want to remove : "))
        if priority in [task.priority for task in tasks]:
            # Implement the logic to remove the task
            task_to_remove = next(task for task in tasks if task.priority == priority)
            print(f"Task with priority '{priority}' with '{task_to_remove.title}' title removed successfully.")
            service.remove_task(priority)
            
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input for priority.")

    print("=======================================================================================")
    
#==================================================================================================================================================

def list_tasks():
    print("=======================================================================================")

    tasks = service.list_tasks()
    if not tasks:
        print("No tasks found.add some tasks to get started!")
    else :
        for task in tasks:
            print(f"{task.priority}. {task.title} (Completed: {task.completed})")

    print("=======================================================================================")

#==================================================================================================================================================

def change_task_info_menu(priority):
    print("=======================================================================================")
    print("1. change title")
    print("2. change description")
    print("3. change priority")
    print("4. back to main menu")
    print("=======================================================================================")
    while True:
        option = input("please select an option to continue : ")
        print()
        try:
            if option == '1':
                while True:
                    new_title = input("enter new title : ")
                    if new_title.strip() == "":
                        print(" empty input is not allowed...try again")
                    else:   
                        error = service.change_task_info(priority, 'title', new_title)
                        if not error:
                            print("A task with this title already exists.please enter a different title.")
                        else :
                            print(f"Task title changed successfully to {new_title}.")
                            list_tasks()
                            break
                break
            elif option == '2':
                    new_description = input("enter new description : ")
                    service.change_task_info(priority, 'description', new_description)
                    list_tasks()
                    break
            elif option == '3':
                while True:
                    try:
                        new_priority = int(input(f"enter new priority (highest == {len(storage.load_tasks())}): "))
                        if new_priority < 1 or new_priority > len(storage.load_tasks()):
                            print("Invalid priority....try again")
                        else:
                            service.change_task_info(priority, 'priority', new_priority)
                            list_tasks()
                            break
                    except ValueError:
                        print("Invalid input for priority...try again")
                break
                            
            elif option == '4':
                return
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input.")
        print("=======================================================================================")
        change_task_info_menu(priority)

#==================================================================================================================================================

def change_task_info():
    list_tasks()
    print("=======================================================================================")
    try:
        tasks = service.list_tasks()
        priority = int(input("enter the priority of task you want to change (enter fo go back): "))
        if priority in [task.priority for task in tasks]:
            change_task_info_menu(priority)
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input for priority.")
    print("=======================================================================================")
    
#==================================================================================================================================================

def complete_task():
    list_tasks()
    print("=======================================================================================")
    try:
        tasks = service.list_tasks()
        priority = int(input("enter the priority of task you want to mark as completed : "))
        if priority in [task.priority for task in tasks]:
            service.change_task_info(priority, 'completed', True)
            print(f"Task with priority '{priority}' marked as completed.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input for priority.")
    list_tasks()
    
def clear_completed_tasks():
    print("=======================================================================================")
    service.clear_completed_tasks()
    print("All completed tasks have been cleared.")
    list_tasks()
    


def show_task_full_info():
    list_tasks()
    print("=======================================================================================")
    try:
        tasks = service.list_tasks()
        priority = int(input("enter the priority of task you want to see its full info : "))
        task = next((task for task in tasks if task.priority == priority), None)
        if task:
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Priority: {task.priority}")
            print(f"Completed: {task.completed}")
            print(f"ID: {task.id}")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input for priority.")
    print("=======================================================================================")
    











def main_menu():
    while True:
        print("===========================================================================================")
        print("1. add tasks")
        print("2. remove tasks")
        print("3. list tasks")
        print("4. change task info")
        print("5. show task full info")
        print("6. complete task")
        print("7. clear completed tasks")
        print("8. exit")
        print("=======================================================================================")
        option = input("please select an option to continue : ")
        if option == '1':
            add_task()
            
        if option == '2':
            remove_task()
            
        if option == '3':
            list_tasks()
        if option == '4':
            change_task_info()
            
        if option == '5':
            show_task_full_info()
            
        if option == '6':
            complete_task()
            
        if option == '7':
            clear_completed_tasks()
            
        if option == '8':
            print("=======================================================================================")
            print("Come back soon for more productivity :)     all your task will be saved and waiting for you when you come back")
            print("=======================================================================================")
            quit()

print("===========================================================================================")
print("==================== wellcome to ' to do list ' terminal based program ====================")
print("====================                  Main Menu                        ====================")
main_menu()