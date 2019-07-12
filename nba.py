class NBA_Player():
    """Instances of NBA_Player represent an NBA Player
    wingspan: int
    name: str"""

    def __init__(self, wingspan: int, name: str) -> None:
        """Initiate NBA_Player
        wingspan = passed-in int
        name = passed-in str
        returns None"""
        
        self.wingspan = wingspan
        self.name = name

class NBA_List():
    """Instance of NBA_List represents a list of NBA_Players
    players: array of NBA_Players"""

    def __init__(self) -> None:
        """Initiate NBA_List
        players = empty array
        returns None"""

        self.players = []

    def add(self, player: NBA_Player) -> None:
        """Add NBA_Player to instance of NBA_List
        returns None"""

        self.players.append(player)

    def get(self, wingspan: int) -> NBA_Player:
        """Get NBA_Player from instance of NBA_List
        returns NBA_Player"""

        # If NBA_Player with inputted wingspan exists, return that NBA_Player
        for i in range(len(self.players)):
            if self.players[i].wingspan == wingspan:
                return self.players[i]

        # If wingpsan is less than NBAPlayer with shortest wingspan, return that NBAPlayer
        if wingspan < self.players[0].wingspan:
            return self.players[0]
        # Else wingspan is greater than NBAPlayer with longest wingspan, return that NBAPlayer
        else:
            return self.players[len(self.players) - 1]

def get_input(text: str) -> str:
    """Get input (str) from user
    returns str"""

    try:
        value = int(text)
        if value < 0:
            return ""
        else:
            return str(value)
    except ValueError:
        return ""

def get_payout(inches: int) -> int:
    """Get payout according to inches (int)
    returns int"""

    # Return 2 to the power of inches removed from wingspan, times 10
    return (2 ** inches) * 10