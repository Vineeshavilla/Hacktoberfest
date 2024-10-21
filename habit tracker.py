import json
import os
from datetime import datetime

class HabitTracker:
    def __init__(self, filename='habits.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def log_habit(self, habit):
        today = str(datetime.today().date())
        if habit not in self.data:
            self.data[habit] = []
        if today not in self.data[habit]:
            self.data[habit].append(today)
            print(f"Logged '{habit}' for today.")
        else:
            print(f"'{habit}' is already logged for today.")
        self.save_data()

    def show_habits(self):
        if not self.data:
            print("No habits logged yet!")
            return
        for habit, dates in self.data.items():
            print(f"Habit: {habit}, Dates: {dates}")

# Example usage
if __name__ == "__main__":
    tracker = HabitTracker()
    while True:
        action = input("Enter action (log/show/exit): ").lower()
        if action == 'log':
            habit = input("Enter habit: ")
            tracker.log_habit(habit)
        elif action == 'show':
            tracker.show_habits()
        elif action == 'exit':
            break
        else:
            print("Invalid action.")
