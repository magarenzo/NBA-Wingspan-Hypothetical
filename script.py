class NBA_Player():
    """Instances of NBA_Player represent an NBA Player
    wingspan: int
    name: str"""

    def __init__(self, wingspan: int, name: str) -> None:
        """Initiate NBA_Player
        wingspan = passed-in int
        name = passed-in str"""
        self.wingspan = wingspan
        self.name = name

class NBA_List():
    """Instance of NBA_List represents a list of NBA_Players
    players: array of NBA_Players"""

    def __init__(self) -> None:
        """Initiate NBA_List
        players = empty array"""

        self.players = []

    def add(self, player: NBA_Player) -> None:
        """Add NBA_Player to instance of NBA_List"""

        self.players.append(player)

    def get(self, wingspan: int) -> NBA_Player:
        """Get NBA_Player from instance of NBA_List"""

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

def get_input(question: str) -> int:
    """Get input (int) from user"""
    
    while True:
        try:
            value = int(input(question))
            if value < 0:
                print("Input must be a positive integer, try again: \n")
                continue
            break
        except ValueError:
            print("Input must be an integer, try again: \n")
            continue

    return value

def get_payout(inches: int) -> int:
    """Get payout according to inches (int)"""

    # Return 2 to the power of inches removed from wingspan, times 10
    return (2 ** inches) * 10

# Driver
# Create instance of NBA_List and fill with NBA_Players
nba_list = NBA_List()
nba_list.add(NBA_Player(73, "Ty Lawson"))
nba_list.add(NBA_Player(74, "Isaiah Thomas"))
nba_list.add(NBA_Player(75, "Allen Iverson"))
nba_list.add(NBA_Player(76, "Stephen Curry"))
nba_list.add(NBA_Player(77, "Steve Nash"))
nba_list.add(NBA_Player(78, "Joe Harris"))
nba_list.add(NBA_Player(79, "Jrue Holiday"))
nba_list.add(NBA_Player(80, "Russell Westbrook"))
nba_list.add(NBA_Player(81, "Jerry West"))
nba_list.add(NBA_Player(82, "Charles Barkley"))
nba_list.add(NBA_Player(83, "Michael Jordan"))
nba_list.add(NBA_Player(84, "LeBron James"))
nba_list.add(NBA_Player(85, "Tony Parker"))
nba_list.add(NBA_Player(86, "Tracy McGrady"))
nba_list.add(NBA_Player(87, "Scottie Pippen"))
nba_list.add(NBA_Player(88, "Bill Russell"))
nba_list.add(NBA_Player(89, "Kevin Durant"))
nba_list.add(NBA_Player(90, "Hakeem Olajuwon"))
nba_list.add(NBA_Player(91, "Shaquille O'Neal"))
nba_list.add(NBA_Player(92, "Kareem Abdul-Jabbar"))
nba_list.add(NBA_Player(93, "Rudy Gobert"))

# Prompt user
current_wingspan = get_input("Enter your current wingspan in inches: \n")
current_player = nba_list.get(current_wingspan)
print("\nYou are currently closest in wingspan to", current_player.name, "who has a wingspan of", current_player.wingspan, "inches\n")

inches = get_input("Enter amount of inches to remove from your wingspan: \n")
if (current_wingspan >= inches):
    new_wingspan = current_wingspan - inches
    new_player = nba_list.get(new_wingspan)
    print("\nYour wingspan is now", new_wingspan, "inches, you earned $", get_payout(inches), "and you are now closest in wingspan to", new_player.name, "who has a wingspan of", new_player.wingspan, "inches")
else:
    print("\nYou cannot remove more inches than the length of your current wingspan")