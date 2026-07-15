# 🐈 DesktopCat

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-In_Development-orange)

A desktop virtual cat that helps you stay on top of your daily schedule.

DesktopCat is a Python desktop application that combines a lightweight virtual pet with a personal task manager. Instead of being just a decorative desktop pet, the cat actively reminds you of upcoming tasks, lets you manage your schedule through a simple interface, and can optionally integrate with a local AI assistant for natural conversations.

---

## ✨ Features

* 🗓️ Create and manage daily tasks
* ⏰ Automatically displays upcoming scheduled tasks
* ✅ Mark tasks as completed with a single click
* 🗑️ Delete or overwrite existing tasks
* 📅 Date-aware scheduling (ignores previous day's tasks)
* 🐈 Animated desktop cat with multiple sprite animations
* 🖱️ Interactive controls using mouse clicks
* 💾 Local JSON-based task storage

## 🛠️ Built With

* Python 3
* Tkinter
* Pillow (PIL)
* JSON

---

## 📂 Project Structure

```text
DesktopCat/
│
├── assets/              # Sprites and UI images
├── src/
│   ├── kitty.py         # Desktop pet animations
│   ├── chatbox.py       # Chat bubble UI
│   ├── scheduleManager.py
│   ├── main.py
│   └── ...
│
├── schedule.json        # Saved tasks
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/DesktopCat.git
cd DesktopCat
```

### 2. Install dependencies

```bash
pip install pillow
```

Tkinter comes pre-installed with most Python installations.

### 3. Run the application

```bash
python src/main.py
```

---

## 📝 Task Format

Tasks are stored locally as JSON.

Example:

```json
{
    "schedule": [
        {
            "date": "2026-07-15",
            "time": "14:00",
            "task": "Study Python",
            "completed": false
        }
    ]
}
```

---

## 🎮 Controls

| Action              | Function                       |
| ------------------- | ------------------------------ |
| Left Button         | Cat moves to the left          |
| Right Button        | Cat moves to the right         |
| Double Middle Click | Open task manager              |
| Complete Button     | Mark current task as completed |


---

