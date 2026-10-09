import os
from dotenv import load_dotenv
from tasks import show_task

load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

open_admin = input("Do you want to open admin mode? yes/no: ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")
        

name = input("Please enter your name: ")

print(f"welcome {name}")

tasks_list = []

while True:
    enter_task_exit = input("Do you want to add a task? (yes/no) ")

    if enter_task_exit == "yes":
        task_question = input("Enter your task: ")
        tasks_list.append(task_question)
        task_priority = input("Enter yout task priority(low, medium, high): ")

        print("Your task has been saved.")

    elif enter_task_exit == "no":
        break

    else:
        print("Error! invalid response, please try again. ")
        continue


show_task(tasks_list, task_priority)

with open("result.txt", "a") as file:
    file.write(f"{name} - Tasks: {tasks_list}\n")