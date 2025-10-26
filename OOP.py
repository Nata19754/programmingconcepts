"""
We will create an object for the NFLTeam.  NFLTeam will have a team name, and a list of players.  We will also create an object for Players.  The Players object will have two attributes, playerName, and playerPosition.
Bit confused on the instructions for the assignment, not sure if done properly.

OOP ASSIGNMENT SMASHMOUTH FOOTBALL
NATALLY CHAVES
Description: This program uses Python objects to create a football team and players.
It demonstrates Object-Oriented Programming  by using 2 classes:
- Player
- NFLTeam

"""

class Player:
    def __init__(self, playerName, playerPosition):
        # Store the player's name and position
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        # Return a readable string for each player
        return f"{self.playerName} - {self.playerPosition}"

class NFLTeam:
    def __init__(self, teamName, players=None):
        # Store the team name and list of players
        self.teamName = teamName
        if players is None:
            self.players = []  # Start with an empty list if not provided
        else:
            self.players = players

    def add_player(self, player):
        # Add a player to the team
        self.players.append(player)

    def print_roster(self):
        # Print the team name and all players
        print(f"Team: {self.teamName}")
        print("Roster:")
        for player in self.players:
            print(" -", player)


def main():
    # Create 4 players for team
    player1 = Player("Joe Montana", "QB")
    player2 = Player("Barry Sanders", "RB")
    player3 = Player("Jerry Rice", "WR")
    player4 = Player("Graham Gano", "K")

    # Add players to a list
    playerList = [player1, player2, player3, player4]

    # Create a team with a name and the list of players
    myTeam = NFLTeam("Natachas Giants", playerList)

    # Output team name and player list
    myTeam.print_roster()


if __name__ == "__main__":
    main()
