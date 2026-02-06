from datetime import datetime


def add_task(tasks):
    titre = input("Quelle est cette tâche ? ")
    reponse = input("Terminée ? (y/n) : ")
    done = reponse == "y"

    date_creation = input("Date de création (YYYY-MM-DD) : ")
    deadline = input("Deadline (YYYY-MM-DD) : ")
    rappel = int(input("Rappel en minutes : "))

    task = {
        "title": titre,
        "done": done,
        "date_creation": date_creation,
        "deadline": deadline,
        "rappel": rappel,
    }

    tasks.append(task)


def show_tasks(tasks):
    i = 1
    while i <= len(tasks):
        task = tasks[i - 1]
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['title']} [{status}]")
        print(f"   Créée le : {task['date_creation']}")
        print(f"   Deadline : {task['deadline']}")
        print(f"   Rappel : {task['rappel']} minutes")
        i += 1


def modify_task(tasks):
    i = 1
    while i <= len(tasks):
        print(f"{i}. {tasks[i - 1]['title']}")
        i += 1

    index = int(input("Numéro de la tâche à modifier : ")) - 1

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
    else:
        print("Tâche inexistante.")
