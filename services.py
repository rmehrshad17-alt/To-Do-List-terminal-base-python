import models
import storage


class ToDoService:
    def __init__(self):
        self.tasks = storage.load_tasks()

    def _save(self):
        storage.save_tasks(self.tasks)

    def task_id(self, title):
        base = title.upper()[:2]
        tasks = self.tasks
        existing_ids = {task.id for task in tasks}
        new_id = base
        suffix = 0
        while new_id in existing_ids:
            suffix += 1
            new_id = f"{base.upper()}{suffix}"
        return new_id

    def list_tasks(self):
        try:
            tasks = self.tasks  
            return sorted(tasks, key=lambda t: t.priority)
        except Exception as e:
            return []

    def add_task(self, title, description, priority=None):
        tasks = self.tasks
        if not tasks:
            default_priority = 1
        else:
            default_priority = len(tasks) + 1

        
            
        if priority == -1:
            priority = default_priority
        elif priority == 0:
            priority = 1
            for task in tasks:
                task.priority += 1
        elif priority <= len(tasks)+1 and priority > -2 :
            for task in tasks:
                if task.priority >= priority:
                    task.priority += 1
        else:
                priority = default_priority
                self._save()
                return False
        

        new_task = models.Task(
            title=title,
            description=description,
            priority=priority,
            id=self.task_id(title)
        )
        tasks.append(new_task)
        self._save()
        return True

    def remove_task(self, priority):
        tasks = self.tasks
        task_to_remove = next((task for task in tasks if task.priority == priority), None)
        if not task_to_remove:
            return False
        tasks.remove(task_to_remove)
        for task in tasks:
            if task.priority > priority:
                task.priority -= 1
        self._save()
        return True

    def change_task_info(self, priority, field, new_value):
        tasks = self.tasks
        task_to_change = next((task for task in tasks if task.priority == priority), None)
        if not task_to_change:
            return False
        if field == 'priority':
            for task in tasks:
                if task.priority >= new_value and task != task_to_change and priority > task.priority:
                    task.priority += 1
        if field == 'title':
            for task in tasks:
                if task.title == new_value:
                    return False
        setattr(task_to_change, field, new_value)
        self._save()
        return True
        

    def complete_task(self, priority):
        self.change_task_info(priority, 'completed', True)
        self._save()
        return True

    def clear_completed_tasks(self):
        tasks = self.tasks
        tasks = [task for task in tasks if not task.completed]
        for index, task in enumerate(tasks):
            task.priority = index + 1
        self._save()
        return True


if __name__ == "__main__":
    pass
