
class Task():
    def __init__(self, title: str, description: str, priority: int, completed: bool=False, id: str=None):        
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.id = id

if __name__ == "__main__":
    pass
