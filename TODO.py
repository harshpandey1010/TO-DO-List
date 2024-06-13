'''
def task():
    tasks = []
    print("-----Welcome to your todo list-----")
    
    total_task = int(input("Enter the number of the task: "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
        
    print(f"Today's task are {tasks} ")
    while True:
        operation = int(input("Enter\n 1-ADD\n 2-DELETE\n 3-UPDATE\n 4-VIEW\n 5-EXIT\n"))
        if operation == 1:
            add = input("Enter task u want to add = ")
            tasks.append(add)
            print(f"Task {add} has been added....")
            
        elif operation == 2:
            del_val= input("Enter the task u want to delete = ")
            if del_val in tasks :
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted")
                
        elif operation == 3:
            updated_val = input("Enter the task you want to update = ")
            if updated_val in tasks:
                up = input("Enter the new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")
                
        elif operation == 4:
            print(f"Total Tasks are = {tasks}")
            
        elif operation == 5:
            print("Closing the program....")
            break
        
task()
'''

import PySimpleGUI as sg

def task():
    tasks = []
    layout = [
        [sg.Text("-----Welcome to your todo list-----")],
        [sg.Text("Enter the number of tasks: "), sg.InputText(size=(10, 1), key='-NUM_TASKS-'), sg.Button('Submit')],
        [sg.Text(size=(50, 1), key='-TASK_LIST-')],
        [sg.Text("Operation: "), sg.Combo(['ADD', 'DELETE', 'UPDATE', 'VIEW', 'EXIT'], size=(10, 1), key='-OPERATION-'), sg.Button('Execute')],
        [sg.Text(size=(50, 1), key='-MESSAGE-')]
    ]

    window = sg.Window('To-Do List', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Submit':
            total_task = int(values['-NUM_TASKS-'])
            for i in range(1, total_task+1):
                task_name = sg.popup_get_text(f"Enter task {i} = ")
                tasks.append(task_name)

            window['-TASK_LIST-'].update(f"Today's tasks are: {tasks}")
        elif event == 'Execute':
            operation = values['-OPERATION-']
            if operation == 'ADD':
                add = sg.popup_get_text("Enter task you want to add = ")
                tasks.append(add)
                window['-MESSAGE-'].update(f"Task '{add}' has been added.")
            elif operation == 'DELETE':
                del_val = sg.popup_get_text("Enter the task you want to delete = ")
                if del_val in tasks:
                    tasks.remove(del_val)
                    window['-MESSAGE-'].update(f"Task '{del_val}' has been deleted.")
                else:
                    window['-MESSAGE-'].update("Task not found.")
            elif operation == 'UPDATE':
                updated_val = sg.popup_get_text("Enter the task you want to update = ")
                if updated_val in tasks:
                    up = sg.popup_get_text("Enter the new task = ")
                    index = tasks.index(updated_val)
                    tasks[index] = up
                    window['-MESSAGE-'].update(f"Task '{updated_val}' has been updated to '{up}'.")
                else:
                    window['-MESSAGE-'].update("Task not found.")
            elif operation == 'VIEW':
                window['-MESSAGE-'].update(f"Total tasks are: {tasks}")
            elif operation == 'EXIT':
                window.close()
                break

    window.close()

task()
