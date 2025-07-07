# Write your solution here
import json

class Statistics:
    def __init__(self, file: str):
        self.file = file
        self.data = self.get_data()

    def get_data(self):
        with open(self.file, "r", encoding="utf8") as f:
            data = json.load(f)
        return data

    def get_player(self, name):
        for player in self.data:
            if player["name"] == name:
                return f"{player['name']:<21}{player['team']} {player['goals']:>3} + {player['assists']:>2} = {player['goals'] + player['assists']:>3}"

    def get_general_information(self, request):
        return [player[request] for player in self.data]


    def get_team_information(self, team):
        return [player for player in self.data if player["team"]==team]

    def get_team_country_info(self, country):
        return [player for player in self.data if player["nationality"]==country]

class ApplicationHandler:
    def __init__(self):
        self.file = input("file name: ")
        self.__stats = Statistics(self.file) 

    def show_length(self):
        return f"read the data of {len(self.__stats.data)} players"

    def search_for_players(self):
        name = input("name: ")
        data = self.__stats.get_player(name)
        print(data)

    def get_general_information(self, cmd):
        if cmd == "2":
            data = sorted(set(self.__stats.get_general_information("team")))
        if cmd == "3":
            data = sorted(set(self.__stats.get_general_information("nationality")))

        for i in data:
            print(i)


    def get_group_players(self, group):
        if group == "team":
            gr = input("team: ")
            team = self.__stats.get_team_information(gr)
        if group == "country":
            gr = input("country: ")
            team = self.__stats.get_team_country_info(gr)

        sorted_players = sorted(team, key=lambda p: p['goals'] + p['assists'], reverse=True)

        for athlete in sorted_players:
            print(self.__stats.get_player(athlete["name"]))

    def get_list_best(self, count):
        numb_athletes = input("how many: ")
        if count == "points":
            sorted_athletes = sorted(self.__stats.data, key=lambda p: -(p['goals'] + p['assists']))
        if count == "goals":
            sorted_athletes = sorted(self.__stats.data, key=lambda p: (-p['goals'], p['games']))

        for athlete in sorted_athletes[:int(numb_athletes)]:
            print(self.__stats.get_player(athlete["name"]))
            

    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        print(self.show_length())
        print("")
        self.help()
        print("")
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_players()
            elif command == "2":
                self.get_general_information(command)
            elif command == "3":
                self.get_general_information(command)
            elif command == "4":
                self.get_group_players("team")
            elif command == "5":
                self.get_group_players("country")
            elif command == "6":
                self.get_list_best("points")
            elif command == "7":
                self.get_list_best("goals")



app = ApplicationHandler()
app.execute()