import json
import time
import uuid
from filelock import FileLock

QUEUE_FILE = "work.txt"
LOCK_FILE = "work.txt.lock"

CONSUMER_ID = str(uuid.uuid4())[:8]

CHECK_INTERVAL = 5
TASK_DURATION = 2


def get_task():
    with FileLock(LOCK_FILE):
        try:
            with open(QUEUE_FILE, "r", encoding="utf-8") as file:
                tasks = [
                    json.loads(line)
                    for line in file
                    if line.strip()
                ]
        except FileNotFoundError:
            return None

        for task in tasks:
            if task["status"] == "pending":
                task["status"] = "in_progress"
                task["consumer_id"] = CONSUMER_ID
                print("Picked up: "+ task["id"])
                with open(QUEUE_FILE, "w") as file:
                    for item in tasks:
                        file.write(
                            json.dumps(item) + "\n"
                        )
                return task
    return None


def finish_task(task_id):
    with FileLock(LOCK_FILE):
        with open(QUEUE_FILE, "r") as file:
            tasks = [
                json.loads(line)
                for line in file
                if line.strip()
            ]

        for task in tasks:
            if (
                task["id"] == task_id
                and task.get("consumer_id") == CONSUMER_ID
            ):
                task["status"] = "done"
                break

        with open(QUEUE_FILE, "w") as file:
            for task in tasks:
                file.write(
                    json.dumps(task) + "\n"
                )

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
