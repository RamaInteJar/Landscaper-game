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

def perform_action(choice):
    global money
    global tools

    action = actions[choice - 1]

    if "cost" in action and action["cost"] > money:
        print("You don't have enough money for this action.")
        return

    if "cost" in action:
        money -= action["cost"]
        tools.append(action["name"])

    money += action["earnings"]

    print(f"\nYou {action['name']} and earned ${action['earnings']}!")

    if money >= win_amount and "team" in tools:
        print(f"\nCongratulations! You've won the game with ${money} and the following tools:")
        for tool in tools:
            print(f"- {tool}")
        quit_game()

# Function to quit the game
def quit_game():
    print("\nThank you for playing!")
    exit()

while True:
    display_actions()
    choice = handle_input()
    perform_action(choice)