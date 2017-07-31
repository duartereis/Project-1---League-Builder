import csv


def separate():
    # opens the file and list all the players in the players variable

    with open('soccer_players.csv', newline='') as csvfile:
        players_reader = csv.DictReader(csvfile, delimiter=',')
        players = list(players_reader)

        # divides the players in experienced and non experienced players and count them

        experienced = []
        fresh = []
        for player in players:
            if player['Soccer Experience'] == 'YES':
                experienced.append(player)
            else:
                fresh.append(player)

        return experienced, fresh, players


def number_of_players():
    experienced, fresh, players = separate()
    players_experience = len(experienced)
    players_fresh = len(fresh)

    return players_experience, players_fresh


def player_team():
    experienced, fresh, players = separate()
    sharks = []
    dragons = []
    raptors = []
    number_teams = 3

    for player in experienced:
        if len(sharks) < number_teams:
            sharks.append(player)
        elif len(dragons) < number_teams:
            dragons.append(player)
        else:
            raptors.append(player)

    for player in fresh:
        if len(sharks) < number_teams * 2:
            sharks.append(player)
        elif len(dragons) < number_teams * 2:
            dragons.append(player)
        else:
            raptors.append(player)

    return sharks, dragons, raptors


def print_teams():
    sharks, dragons, raptors = player_team()

    with open('teams.txt', 'w') as file:

        file.write("Sharks\n\n")
        for player in sharks:
            row = player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n'
            file.write(row)

        file.write("\n\nRaptors\n\n")
        for player in raptors:
            row = player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n'
            file.write(row)

        file.write("\n\nDragons\n\n")
        for player in dragons:
            row = player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n'
            file.write(row)


def print_letters():
    experienced, fresh, players = separate()
    sharks, dragons, raptors = player_team()

    for player in players:

        name = "_".join(player["Name"].split()).lower()

        filename = name + ".txt"

        if player in sharks:
            team = "Sharks"
        elif player in dragons:
            team = "Dragons"
        else:
            team = "Raptors"

        with open(filename, 'w') as file:
            file.write("Dear {},\n\n"
                       "Your son {} was selected to play for the {} team.\n\n"
                       "Next practice will be at 12pm on the 14th of August, 2017.\n\n"
                       "Hope to see you there.\n\n"
                       "Best regards,\n\n"
                       "Soccer League Generator".format(player["Guardian Name(s)"], player["Name"], team))


print("Welcome to the Soccer League Generator!\n"
      "At this time, we only have 3 teams available for your players.\n"
      "We will do our best to equally distribute the number of experienced players among the teams.\n")

if __name__ == "__main__":
    while True:
        start = input("Want to start? (Y/n) ").lower()
        if start == "y":
            players_experience, players_fresh = number_of_players()
            if players_experience % 3 != 0:
                print("you have {} experienced players. We can't split them equally by the 3 teams\n"
                      "Please talk with some friends, add them to your list!".format(players_experience))
            elif players_fresh % 3 != 0:
                print("you have {} non-experienced players. We can't split them equally by the 3 teams\n"
                      "Please talk with some friends, add them to your list!".format(players_fresh))
            else:
                print_teams()
                print("A .txt file was created with the final 3 teams for the tournament!\n")
                letter = input("Do you wish to generate a letter for every guardian's player? (Y/n) ").lower()
                while True:
                    if letter == "y":
                        print_letters()
                        break
                    elif letter == "n":
                        "See you later"
                        break
                    else:
                        print("Command not accepted! Please write 'Y' to start or 'N' to not send the letters!\n")

            break
        elif start == "n":
            print("See you later!")
            break
        else:
            print("Command not accepted! Please write 'Y' to start or 'N' to exit!\n")
