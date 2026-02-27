import models
import csv
import os


def save_tasks(tasks):
    try:
        with open('tasks.csv', mode='w', newline='') as file:
            fieldnames = ['id', 'title', 'description', 'priority', 'completed']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow({
                    'id': str(task.id) if task.id is not None else '',
                    'title': task.title,
                    'description': task.description,
                    'priority': task.priority,
                    'completed': str(task.completed)
                })
    except IOError :
        pass

def load_tasks():
    tasks = []
    if not os.path.exists('tasks.csv'):
        return tasks
    try:
        with open('tasks.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    priority = int(row.get('priority', 1))
                except ValueError:
                    priority = 0
                completed = row.get('completed', 'False') == 'True'
                task = models.Task(
                    title=row.get('title', ''),
                    description=row.get('description', ''),
                    priority=priority,
                    completed=completed,
                    id=row.get('id')
                )
                tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks

if __name__ == "__main__":
    pass