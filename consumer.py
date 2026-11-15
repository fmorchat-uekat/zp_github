import sqlite3
import time
import uuid

CONSUMER_ID = str(uuid.uuid4())[:8]

CHECK_INTERVAL = 5
TASK_DURATION = 2

con = sqlite3.connect('database.db')
cur = con.cursor()


def get_task():
    cur.execute("""
                SELECT id, task, status
                FROM tasks
                WHERE status = 'pending'
                LIMIT 1
            """)
    task = cur.fetchone()

    if task is None:
        return None

    task_id, task_name, status = task
    cur.execute("""
                UPDATE tasks
                SET status = 'in_progress',
                    consumer_id = ?
                WHERE id = ?
                  AND status = 'pending'
            """, (CONSUMER_ID, task_id))
    if cur.rowcount != 1:
        return None

    con.commit()
    print("Picked up:", task_id)
    return {
        "id": task_id,
        "task": task_name,
        "status": "in_progress",
        "consumer_id": CONSUMER_ID
    }


def finish_task(task_id):
    cur.execute("""
                UPDATE tasks
                SET status = 'done'
                WHERE id = ?
                  AND consumer_id = ?
                  AND status = 'in_progress'
            """, (task_id, CONSUMER_ID))

    con.commit()

    if cur.rowcount == 1:
        print("Finished:", task_id)
    else:
        print("Could not finish:", task_id)

def execute_task(task):
    time.sleep(TASK_DURATION)
    finish_task(task["id"])

def main():
    print(CONSUMER_ID)
    while True:
        task = get_task()
        if task:
            execute_task(task)
        else:
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
