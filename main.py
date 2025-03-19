import random

def calculate_lucky_numbers(is_home):
    lucky_numbers = []
    if is_home:
        while len(lucky_numbers) < 7:
            lucky_number = random.randint(0,100)
            if lucky_number not in lucky_numbers:
                lucky_numbers.append(lucky_number)
    else:
        while len(lucky_numbers) < 5:
            lucky_number = random.randint(0,100)
            if lucky_number not in lucky_numbers:
                lucky_numbers.append(lucky_number)

    return lucky_numbers

home_lucky_numbers = calculate_lucky_numbers(True)
away_lucky_numbers = calculate_lucky_numbers(False)

away_team ="Real Madrid"
home_team = "Barcelona"


def play_match(home_team, away_team, home_lucky_numbers, away_lucky_numbers):
    home_goals = 0
    away_goals = 0
    winner = "Nobody"
    for i in range(90):
        if random.randint(0,100) in home_lucky_numbers:
            home_goals = home_goals + 1
            print(f"{i} minutes, {home_team} has scored a Goal, the result is {home_goals} x {away_goals}")
        elif random.randint(0,100)in away_lucky_numbers:
            away_goals = away_goals + 1
            print(f"{i} minutes, {away_team} has scored a Goal, the result is {home_goals} x {away_goals}")

    if home_goals > away_goals:
        winner = home_team
    elif away_goals > home_goals:
        winner = away_team
    print(f"Final result is {home_goals} x {away_goals}, congratulations to {winner}!")

play_match(home_team, away_team, home_lucky_numbers, away_lucky_numbers)