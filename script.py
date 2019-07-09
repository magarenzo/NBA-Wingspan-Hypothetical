# NBAPlayer
class NBAPlayer():

  #Initiate NBAPlayer
  def __init__(self, w: int, n: str) -> None:

    self.wingspan = w
    self.name = n

# NBAList
class NBAList():

    # Initiate NBAList
    def __init__(self) -> None:

        self.players = []

    # Add NBAPlayer to NBAList
    def add(self, n: NBAPlayer) -> None:

        self.players.append(n)

    # Get NBAPlayer from NBAList of specified wingspan
    def get(self, w: int) -> str:

    
        for i in range(len(self.players)):
            if self.players[i].wingspan == w:
                return self.players[i]

        if w < self.players[0].wingspan:
            return self.players[0]
        else:
            return self.players[len(n)]

# Get Payout
def getPayout(inches):

    # Return 2 to the power of inches removed from wingspan, times 10
    return (2 ** inches) * 10

# Driver
# Create instance of NBAList and fill with NBAPlayers
n = NBAList()
n.add(NBAPlayer(73, "Ty Lawson"))
n.add(NBAPlayer(74, "Isaiah Thomas"))
n.add(NBAPlayer(75, "Allen Iverson"))
n.add(NBAPlayer(76, "Stephen Curry"))
n.add(NBAPlayer(77, "Steve Nash"))
n.add(NBAPlayer(78, "Joe Harris"))
n.add(NBAPlayer(79, "Jrue Holiday"))
n.add(NBAPlayer(80, "Russell Westbrook"))
n.add(NBAPlayer(81, "Jerry West"))
n.add(NBAPlayer(82, "Charles Barkley"))
n.add(NBAPlayer(83, "Michael Jordan"))
n.add(NBAPlayer(84, "LeBron James"))
n.add(NBAPlayer(85, "Tony Parker"))
n.add(NBAPlayer(86, "Tracy McGrady"))
n.add(NBAPlayer(87, "Scottie Pippen"))
n.add(NBAPlayer(88, "Bill Russell"))
n.add(NBAPlayer(89, "Kevin Durant"))
n.add(NBAPlayer(90, "Hakeem Olajuwon"))
n.add(NBAPlayer(91, "Shaquille O'Neal"))
n.add(NBAPlayer(92, "Kareem Abdul-Jabbar"))
n.add(NBAPlayer(93, "Rudy Gobert"))

# Prompt user
current = int(input("What is your current wingspan in inches?\n"))
currentPlayer = n.get(current)
print("\nYou are currently closest in wingspan to", currentPlayer.name, "who has a wingspan of", currentPlayer.wingspan, "inches\n")

inches = int(input("How many inches do you want to remove from your wingspan?\n"))
if (current >= inches):
    newPlayer = n.get(current - inches)
    print("\nYour wingspan is now", current - inches, "inches, you earned $", getPayout(inches), "and you are now closest in wingspan to", newPlayer.name, "who has a wingspan of", newPlayer.wingspan, "inches")
else:
    print("\nYou cannot remove more inches than the length of your current wingspan")