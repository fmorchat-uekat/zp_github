import uuid
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

def produce_task():
    task = {
        "id": str(uuid.uuid4()),
        "task": "Rozmowa telefoniczna",
        "status": "pending"
    }

    cur.execute(f"INSERT INTO tasks VALUES('"
                f"{task.get('id')}','"
                f"{task.get('task')}','"
                f"{task.get('status')}',NULL)")
    con.commit()

    print(f"Dodano zadanie: {task['id']}")

if __name__ == "__main__":
    produce_task()
