import json
import uuid

QUEUE_FILE = "work.txt"


def produce_task():
    task = {
        "id": str(uuid.uuid4()),
        "task": "Rozmowa telefoniczna",
        "status": "pending"
    }

    with open(QUEUE_FILE, "a") as file:
        file.write(json.dumps(task) + "\n")

    print(f"Dodano zadanie: {task['id']}")


if __name__ == "__main__":
    for i in range(100):
        produce_task()
