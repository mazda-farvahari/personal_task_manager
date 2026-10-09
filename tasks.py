

def show_task(tasks, task_priority):
    print("  ")
    print("---Tasks---")
    n = 1

    for i in tasks:
        print(f"    Task {n} : {i}")
        print(f"    Task {n} priority : {task_priority}")
        print(" ")
        n += 1

