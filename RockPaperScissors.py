# RockPaperScissors
import getpass

x = 0   # Keeps track of player X's current selection
y = 0   # Keeps track of player Y's current selection
x_wins = 0  # Keeps track of player X's overall wins
y_wins = 0  # Keeps track of player Y's overall wins
num_games = 2  # Player X will first choose and then player Y according to the following keys 
keep_playing = True  # Will get set to false when there is a winner 
valid_input = False  # Checks to make sure the user input a 1, 2, or 3 as well as if the num games needed is valid


while (valid_input == False):
	num_games = str(raw_input("Choose number of games (1-9) needed in order to win: "))
	if (num_games != "1" and num_games != "2" and num_games != "3" and num_games != "4" and num_games != "5"
	and num_games != "6" and num_games != "7" and num_games != "8" and num_games != "9"):
		print("Incorrect selection, please select 1-9 games to win")
	else:
		valid_input = True
		num_games = int(num_games)
 
print ("\nPlayer X will first choose and then player Y according to the following keys")

print("	1 = Rock")
print("	2 = Paper")
print("	3 = Scissors")

while (keep_playing == True):

	valid_input = False
	while (valid_input == False):
		x = str(getpass.getpass("Player X, choose your item: "))
		if (x != "1" and x != "2" and x != "3"):
			print("You did not enter a valid input, please use 1, 2, or 3")
		else:
			valid_input = True

	valid_input = False
	while (valid_input == False):
		y = str(getpass.getpass("Player Y, choose your item: "))
		if (y != "1" and y != "2" and y != "3"):
			print("You did not enter a valid input, please use 1, 2, or 3")
		else:
			valid_input = True
	
	x = int(x)
	y = int(y)
	if (x == y):
		print("\nBoth players chose the same item, please choose again")
	elif (x == 1 and y == 2):
		print("\nPlayer X chose Rock and Player Y chose Paper. Player Y wins this round")
		y_wins = y_wins + 1
	elif (x == 1 and y == 3):
		print("\nPlayer X chose Rock and Player Y chose Scissors.  Player X wins this round")
		x_wins = x_wins + 1
	elif (x == 2 and y == 3):
		print("\nPlayer X chose Paper and Player Y chose Scissors.  Player Y wins this round")
		y_wins = y_wins + 1		
	elif (x == 2 and y == 1):
		print("\nPlayer X chose Paper and Player Y chose Rock.  Player X wins this round")
		x_wins = x_wins + 1
	elif (x == 3 and y == 1):
		print("\nPlayer X chose Scissors and Player Y chose Rock.  Player Y wins this round")
		y_wins = y_wins + 1
	elif (x == 3 and y == 2):
		print("\nPlayer X chose Scissors and Player Y chose Papaer.  Player X wins this round")
		x_wins = x_wins + 1

 	print("")
	print("Wins:")
	print("	Player X: " + str(x_wins))
	print("	Player Y: " + str(y_wins))
	print("")

	if (x_wins == num_games):
		print("Player X Wins!")
		print("")
		keep_playing = False

	if (y_wins == num_games):
		print("Player Y Wins!")
		print("")
		keep_playing = False