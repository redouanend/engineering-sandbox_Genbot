from datetime import datetime
from functions import add_task, show_tasks, modify_task
import json
from pathlib import Path

fichier = Path("./task_manager/tasks.json")
with open(fichier, "r", encoding="utf-8") as f:
    tasks = json.load(f)

today = datetime.today()

running = True

for task in tasks:
    deadline_date = datetime.strptime(task["deadline"], "%Y-%m-%d")
    jours_restants = (deadline_date - today).days

    if jours_restants >= 0:
        print(
            f"🔔 Rappel : '{task['title']}' → "
            f"{jours_restants} jour(s) restant(s) avant la deadline"
        )
    else:
        print(
            f"⚠️  Deadline dépassée pour '{task['title']}' "
            f"({abs(jours_restants)} jour(s) de retard)"
        )

while running:
    print("What do you want to do?\n")
    choix = input("Add / Show / Modify / Quit")

    if choix == "Add":
        add_task(tasks)
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)

    elif choix == "Show":
        show_tasks(tasks)

    elif choix == "Modify":
        modify_task(tasks)
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)

    elif choix == "Quit":
        running = False