import random
import time

ronaldo = {
    "name": "Cristiano Ronaldo",
    "age": 35,
    "team": "Portugal",
    "club": "Real Madrid",
    "position": "Forward",
    "stats":{
        "shooting": 95,
        "dribbling": 90,
        "passing": 80,
        "defending": 45,
        "physical": 85,
        "speed": 85,
    }
}

messi = {
    "name": "Lionel Messi",
    "age": 33,
    "team": "Argentina",
    "club": "Barcelona",
    "position": "Forward",
    "stats":{
        "shooting": 95,
        "dribbling": 95,
        "passing": 95,
        "defending": 40,
        "physical": 75,
        "speed": 90,
    }
}

neymar = {
    "name": "Neymar Jr",
    "age": 28,
    "team": "Brazil",
    "club": "Barcelona",
    "position": "Forward",
    "stats":{
        "shooting": 99,
        "dribbling": 99,
        "passing": 99,
        "defending": 99,
        "physical": 99,
        "speed": 99,
    }
}
bale = {
    "name": "Gareth Bale",
    "age": 31,
    "team": "Wales",
    "club": "Real Madrid",
    "position": "Forward",
    "stats":{
        "shooting": 90,
        "dribbling": 85,
        "passing": 75,
        "defending": 50,
        "physical": 80,
        "speed": 95,
    }
}

real_madrid = {
    "name": "Real Madrid",
    "players": [ronaldo, bale],
    "stadium": "Santiago Bernabeu",
}
barcelona = {
    "name": "Barcelona",
    "players": [messi, neymar],
    "stadium": "Camp Nou",
}

def get_player_overall(player):        
    stats = player["stats"]
    overall = (stats["shooting"] + stats["dribbling"] + stats["passing"] + stats["defending"] + stats["physical"] + stats["speed"]) / 6
    return overall


def get_team_overall(team):
    overall = 0
    for player in team["players"]:
        overall = overall + get_player_overall(player)
    return overall / len(team["players"])

def calculate_lucky_numbers(home_team, away_team):
    home_lucky_numbers = []
    away_lucky_numbers = []
    while len(home_lucky_numbers) < round(5 * (1 + get_team_overall(home_team) / 100)):
            lucky_number = random.randint(0,100)
            if lucky_number not in home_lucky_numbers:
                home_lucky_numbers.append(lucky_number)
    else:
        while len(away_lucky_numbers) < round(4* (1 + get_team_overall(away_team) / 100)):
            lucky_number = random.randint(0,100)
            if lucky_number not in away_lucky_numbers:
                away_lucky_numbers.append(lucky_number)

    return home_lucky_numbers, away_lucky_numbers

def player_scored(team_players):
    striker_array = []
    not_striker_array = []
    chance_array = []
    for player in team_players:
        if player["position"] == "Forward":
            striker_array.append(player["name"])
        else:
            not_striker_array.append(player["name"])
    chance_array = striker_array + not_striker_array
    the_man = random.choice(chance_array)
    return the_man


def play_match(real_madrid, barcelona, location):
    if location == real_madrid["stadium"]:
        home_team = real_madrid
        away_team = barcelona
    else:
        home_team = barcelona
        away_team = real_madrid
    
    home_players = home_team["players"]
    away_players = away_team["players"]
    home_goals = 0
    away_goals = 0
    winner = "Nobody"

    home_lucky_numbers, away_lucky_numbers = calculate_lucky_numbers(home_team=home_team, away_team=away_team)
    for i in range(90):
        if random.randint(0,100) in home_lucky_numbers:
            home_goals = home_goals + 1
            print(f"{i} minutes,\n {player_scored(home_players)} \n {home_team['name']} has scored a Goal, the result is {home_goals} x {away_goals}")
            time.sleep(2)
        elif random.randint(0,100)in away_lucky_numbers:
            away_goals = away_goals + 1
            print(f"{i} minutes, \n {player_scored(away_players)} \n {away_team['name']} has scored a Goal, the result is {home_goals} x {away_goals}")
            time.sleep(2)
    if home_goals > away_goals:
        winner = home_team["name"]
    elif away_goals > home_goals:
        winner = away_team["name"]
    print(f"Final result is {home_goals} x {away_goals}, congratulations to {winner}!")

play_match(real_madrid, barcelona, "Camp Nou")