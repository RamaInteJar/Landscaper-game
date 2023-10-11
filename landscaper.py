money = 0
tools = []
win_amount = 1000

# Define actions
actions = [
    {"name": "Cut grass with teeth", "earnings": 1},
    {"name": "Buy rusty scissors", "cost": 5, "earnings": 5},
    {"name": "Use rusty scissors", "earnings": 5},
    {"name": "Buy old-timey push lawnmower", "cost": 25, "earnings": 50},
    {"name": "Use old-timey push lawnmower", "earnings": 50},
    {"name": "Buy fancy battery-powered lawnmower", "cost": 250, "earnings": 100},
    {"name": "Use fancy battery-powered lawnmower", "earnings": 100},
    {"name": "Hire a team of starving students", "cost": 500, "earnings": 250},
    {"name": "Use a team of starving students", "earnings": 250}
]

def display_actions():
    print("\nAvailable Actions:")
    for i, action in enumerate(actions):
        print(f"{i + 1}. {action['name']}")

def handle_input():
    while True:
        try:
            choice = int(input("\nEnter your choice (or 0 to quit): "))
            if choice == 0:
                quit_game()
            elif 1 <= choice <= len(actions):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
