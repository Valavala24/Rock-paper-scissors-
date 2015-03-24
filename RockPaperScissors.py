# RockPaperScissors

x = 0
y = 0
x_wins = 0
y_wins = 0
num_games = 2  # Player X will first choose and then player Y according to the following keys 

print("	1 = Rock")
print("	2 = Paper")
print("	3 = Scissors")

x = int(x)
y = int(y)
	if (x == y):
	elif (x == 1 and y == 2): # Player X chose Rock and Player Y chose Paper. Player Y wins this round
		y_wins = y_wins + 1
	elif (x == 1 and y == 3)  # Player X chose Rock and Player Y chose Scissors.  Player X wins this round
		x_wins = x_wins + 1
	elif (x == 2 and y == 3) # Player X chose Paper and Player Y chose Scissors.  Player Y wins this round")
		y_wins = y_wins + 1		
	elif (x == 2 and y == 1)  # Player X chose Paper and Player Y chose Rock.  Player X wins this round")
		x_wins = x_wins + 1
	elif (x == 3 and y == 1)  # Player X chose Scissors and Player Y chose Rock.  Player Y wins this round")
		y_wins = y_wins + 1
	elif (x == 3 and y == 2)  # Player X chose Scissors and Player Y chose Papaer.  Player X wins this round")
		x_wins = x_wins + 1
