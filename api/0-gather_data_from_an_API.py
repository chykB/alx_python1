import requests
import sys

if len(sys.argv) != 2:
    sys.exit(1)

employee_id = int(sys.argv[1])

employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

employee_response = requests.get(employee_url)
todos_response = requests.get(todos_url)

if employee_response.status_code != 200 or todos_response.status_code != 200:
    sys.exit(1)

employee_data = employee_response.json()
todo_data = todos_response.json()
employee_name = employee_data.get("name", "")

tasks_completed = 0
total_tasks = 0
for task in todo_data:
    if task["completed"]:
        tasks_completed += 1
    total_tasks += 1


print(f"Employee {employee_name} is done with tasks ({tasks_completed}/{total_tasks}):")

for task in todo_data:
    print(f"\t{task['title']}")

