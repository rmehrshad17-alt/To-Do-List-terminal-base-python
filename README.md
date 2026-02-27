


# 📝 Terminal Based To-Do List Manager

A simple yet structured terminal-based To-Do List application written in Python.

This project was built as a practice project with clean architecture principles in mind and separation of concerns between layers.

---

## 🚀 Features

- Add tasks with dynamic priority positioning
- Automatic priority re-indexing
- Remove tasks
- Change task information (title, description, priority)
- Mark tasks as completed
- Clear completed tasks
- View full task details
- Persistent storage using CSV
- Automatic unique task ID generation

---

## 🏗 Project Structure
├── main.py # UI Layer (Terminal interaction)
├── services.py # Business Logic Layer
├── storage.py # Persistence Layer (CSV handling)
├── models.py # Data Model
└── tasks.csv # Stored tasks

---

## 🧠 Architecture

The project follows a layered architecture:

- **Model Layer** → Defines Task object
- **Storage Layer** → Handles CSV read/write
- **Service Layer** → Contains business logic
- **UI Layer (main)** → Handles user interaction

This separation improves maintainability and scalability.

---

## 💾 Storage

Tasks are stored in a `tasks.csv` file using Python's built-in `csv` module.

Each task contains:

- id
- title
- description
- priority
- completed (boolean)

---

## ▶️ How to Run

```bash
python main.py

📌 Requirements

Python 3.8+

📈 Future Improvements

Add unit tests

Convert to SQLite instead of CSV

Add due dates

Add search functionality

Convert to GUI or Web version

👨‍💻 Author

Mehrshad Rezaei

📄 License

This project is open-source and available for educational purposes.
