import random

def get_user_choice():
    print("enter: ")
    print("1: ✊✊✊")
    print("2: ✋✋✋")
    print("3: ✌️✌️✌️")
    choice = input(" rnter the (1/2/3): ")
    return int(choice)

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user, computer):
    outcomes = {
        (1, 3): "فزت! الحجر يكسر المقص.",
        (3, 2): "فزت! المقص يقطع الورقة.",
        (2, 1): "فزت! الورقة تغطي الحجر.",
    }
    if user == computer:
        return "%50!"
    elif (user, computer) in outcomes:
        return outcomes[(user, computer)]
    else:
        return "🕳🕳🕳!"

choices_map = {1: "✊✊✊", 2: "✋✋✋", 3: "✌️✌️✌️"}

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nاختيارك: {choices_map[user_choice]}")
    print(f"اختيار الكمبيوتر: {choices_map[computer_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")

play_game()