
tasks_list = []

def show_task(tasks):
    print("  ")
    print("---Tasks---")
    n = 1

    for i in tasks:
        print(f"    Task {n} : {i}")
        n += 1

name = input("Please enter your name: ")

print(f"welcome {name}")


while True:
    enter_task_exit = input("Do you want to add a task? (yes/no) ")

    if enter_task_exit == "yes":
        task_question = input("Enter your task: ")
        tasks_list.append(task_question)

        print("Your task has been saved.")

    elif enter_task_exit == "no":
        break

    else:
        print("Error! invalid response, please try again. ")
        continue


show_task(tasks_list)