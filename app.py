import nba
from flask import Flask, request, url_for, render_template, render_template_string
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    """Home at /
    returns template"""

    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    """Home at /
    returns template to / with data"""

    # Create instance of NBA_List
    nba_list = nba.NBA_List()

    # Fill NBA_List with NBA_Players
    nba_list.add(nba.NBA_Player(73, "Ty Lawson"))
    nba_list.add(nba.NBA_Player(74, "Isaiah Thomas"))
    nba_list.add(nba.NBA_Player(75, "Allen Iverson"))
    nba_list.add(nba.NBA_Player(76, "Stephen Curry"))
    nba_list.add(nba.NBA_Player(77, "Steve Nash"))
    nba_list.add(nba.NBA_Player(78, "Joe Harris"))
    nba_list.add(nba.NBA_Player(79, "Jrue Holiday"))
    nba_list.add(nba.NBA_Player(80, "Russell Westbrook"))
    nba_list.add(nba.NBA_Player(81, "Jerry West"))
    nba_list.add(nba.NBA_Player(82, "Charles Barkley"))
    nba_list.add(nba.NBA_Player(83, "Michael Jordan"))
    nba_list.add(nba.NBA_Player(84, "LeBron James"))
    nba_list.add(nba.NBA_Player(85, "Tony Parker"))
    nba_list.add(nba.NBA_Player(86, "Tracy McGrady"))
    nba_list.add(nba.NBA_Player(87, "Scottie Pippen"))
    nba_list.add(nba.NBA_Player(88, "Bill Russell"))
    nba_list.add(nba.NBA_Player(89, "Kevin Durant"))
    nba_list.add(nba.NBA_Player(90, "Hakeem Olajuwon"))
    nba_list.add(nba.NBA_Player(91, "Shaquille O'Neal"))
    nba_list.add(nba.NBA_Player(92, "Kareem Abdul-Jabbar"))
    nba_list.add(nba.NBA_Player(93, "Rudy Gobert"))

    # Driver
    # Store form input
    wingspan = request.form["wingspan"]
    inches = request.form["inches"]
    current_wingspan = nba.get_input(wingspan.upper())
    inches = nba.get_input(inches.upper())

    # Return template with error message if necessary
    if current_wingspan == "":
        return render_template("index.html", wingspanErrorString="Input must be a positive integer, try again:")
    if inches == "":
        return render_template("index.html", inchesErrorString="Input must be a positive integer, try again:")

    # If input is appropriate, return template with data
    if int(current_wingspan) >= int(inches):
        current_player = nba_list.get(int(current_wingspan))
        current_player_string = render_template_string("You are currently closest in wingspan to {{ name }}, who has a wingspan of {{ wingspan }} inches.", name=current_player.name, wingspan=current_player.wingspan)
        new_wingspan = int(current_wingspan) - int(inches)
        new_player = nba_list.get(int(new_wingspan))
        payout = nba.get_payout(int(inches))
        new_player_string = render_template_string("Your new wingspan is {{ wingspan }} inches, you earned ${{ payout }}, and you are now closest in wingspan to {{ name }}, who has a wingspan of {{ newWingspan }} inches.", wingspan=new_wingspan, payout=payout, name=new_player.name, newWingspan=new_player.wingspan)
        return render_template("index.html", currentPlayerString=current_player_string, newPlayerString=new_player_string)
    # Else return template with error message
    else:
        return render_template("index.html", mathErrorString="You cannot remove more inches than the length of your current wingspan")
    return render_template("index.html", currentPlayerString=current_player_string)
    
# Run the app
if __name__ == "__main__":
    app.run()