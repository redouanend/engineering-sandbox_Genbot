from datetime import datetime
import json
from pathlib import Path

fichier = Path("tasks.json")
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
        titre = input("quel est cette tache ? ")
        reponse = input("Terminé ? (y/n) : ")
        conv = reponse == "y"

        date_creation = input("Date de création (YYYY-MM-DD) : ")
        deadline = input("Deadline (YYYY-MM-DD) : ")
        rappel = int(input("Rappel en minutes : "))

        task = {
            "title": titre,
            "done": conv,
            "date_creation": date_creation,
            "deadline": deadline,
            "rappel": rappel,
        }
        tasks.append(task)
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)

    elif choix == "Show":
        i = 1
        while i <= len(tasks):
            task = tasks[i - 1]
            status = "✔" if task["done"] else "✘"
            print(f"{i}. {task['title']} [{status}]")
            print(f"   Créée le : {task['date_creation']}")
            print(f"   Deadline : {task['deadline']}")
            print(f"   Rappel : {task['rappel']} minutes")
            i += 1

    elif choix == "Modify":
        i = 1
        while i <= len(tasks):
            print(f"{i}. {tasks[i - 1]['title']}")
            i += 1

        index = int(input("Numéro de la task à modifier : ")) - 1

        if 0 <= index < len(tasks):
            task = tasks[index]

            print("\nQue veux-tu modifier ?")
            print("1. Titre")
            print("2. Terminé")
            print("3. Date de création")
            print("4. Deadline")
            print("5. Rappel")

            choix_modif = input("Choix : ")

            if choix_modif == "1":
                task["title"] = input("Nouveau titre : ")

            elif choix_modif == "2":
                rep = input("Terminé ? (y/n) : ")
                task["done"] = rep == "y"

            elif choix_modif == "3":
                task["date_creation"] = input("Nouvelle date de création : ")

            elif choix_modif == "4":
                task["deadline"] = input("Nouvelle deadline : ")

            elif choix_modif == "5":
                task["rappel"] = int(input("Nouveau rappel (minutes) : "))

            else:
                print("Choix invalide.")
            
            with open(fichier, "w", encoding="utf-8") as f:
                json.dump(tasks, f, indent=4, ensure_ascii=False)

        else:
            print("Task inexistante.")

    elif choix == "Quit":
        running = False
