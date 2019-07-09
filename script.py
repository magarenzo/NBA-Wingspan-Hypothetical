# Get Payout
def getPayout(inches):

    return (2 ** inches) * 10

# Create array
nba = []
nba.insert(73, "Ty Lawson")
nba.insert(74, "Isaiah Thomas")
nba.insert(75, "Allen Iverson")
nba.insert(76, "Stephen Curry")
nba.insert(77, "Steve Nash")
nba.insert(78, "Joe Harris")
nba.insert(79, "Jrue Holiday")
nba.insert(80, "Russell Westbrook")
nba.insert(81, "Jerry West")
nba.insert(82, "Charles Barkley")
nba.insert(83, "Michael Jordan")
nba.insert(84, "LeBron James")
nba.insert(85, "Tony Parker")
nba.insert(86, "Tracy McGrady")
nba.insert(87, "Scottie Pippen")
nba.insert(88, "Bill Russell")
nba.insert(89, "Kevin Durant")
nba.insert(90, "Hakeem Olajuwon")
nba.insert(91, "Shaquille O'Neal")
nba.insert(92, "Kareem Abdul-Jabbar")
nba.insert(93, "Rudy Gobert")

# Start of Driver
current = int(input("What is your current wingspan in inches?\n"))
inches = int(input("How many inches do you want to remove from your wingspan?\n"))

if (inches <= current):
    print("Your wingspan is now", current - inches, "inches, and you earned $", getPayout(inches))
else:
    print("You cannot remove more inches than the length of your current wingspan")