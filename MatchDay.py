# for all things matchday
#
#
#                                          _______ 
#                              ____________|#####|_____________
#                             /    /     /_________\      \    \
#                            /    /           .            \    \
#                           /    /__________________________\    \
#                          /                                      \
#                         /                                        \
#                        /                                          \
#
#
#
#        _________________________________________________________________________
#       |                                    |                                    |
#       |                                    |                                    |
#       |                                    |                                    |
#       |‾‾‾‾‾‾‾‾‾‾‾‾|                       |                       |‾‾‾‾‾‾‾‾‾‾‾‾|
#       |            |                 /|‾‾‾‾‾‾‾‾‾|\                 |            |
#       |‾‾‾‾‾|      |               /‾‾‾         ‾‾‾\               |      |‾‾‾‾‾|
#       |     |      |              |                 |              |      |     |
#       |     |  .   |              |        @        |              |   .  |     |
#       |     |      |              |                 |              |      |     |
#       |_____|      |               \___         ___/               |      |_____|
#       |            |                 \|_________|/                 |            |
#       |____________|                       |                       |____________|
#       |                                    |                                    |
#       |                                    |                                    |
#       |                                    |                                    |
#        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
#
#
#
#                                                        |>
#  ______________________________________________________|
#                                                        \
#                                                         \                 /|
#                                                          \               / |
#                                                           \   |\########\  |
#                                   \‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\  |#\########\ |
#                                    \                        \ |##\########\|
# ‾‾‾‾\                               \                        \|###\########\
#       ‾‾\_                          /\               _________\    \########\   
#           \                        /  \              \         \    \########\ ______
#    .       \                       |   \      .       \         \    |########|      |  
#             \                       |   \              \         \   |########|      |
#              |                       \   \              \         \  |########|      |
#              |                         \  \              ‾‾‾‾‾‾‾‾‾‾\ |########|      |
#            _/                            \ \                        \ ‾‾‾‾‾‾‾‾       |
#   ________/                                \\                        \               |
#      \                                       \                        \              |
#       \                                       \                        \
#        \                                       \________________________\
#         \                                                                \
#          \                                                                \
#           \                                                                \
#            \                                                                \ |>
#             \                                                                \|
#              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

import math
import time as t
import random as r
import Generation 

TeamSheet1 = [] #when team sheets are generated the player names go into the lists
TeamSheet2 = []
TeamSheet3 = []
TeamSheet4 = []
UserTeam = []

CommentatorWords = {
  "Descript": ["amazing ", "sublime ", "incredible ", "stunning ", "sensational ", "awe inspiring ", "easy ", "simple ", "effortless ", "straight forward ", "fundamental "],
  "type": ["rocket ", "shot ", "bicycle kick ", "scissor kick ", "rabona ", "tap in ", "chip "],
  "area": ["top left corner ", "bottom left corner ", "top right corner ", "bottom right corner "]
}
#this is so commentary is not all the same

LeagueTable = {
	"Team 1" : 0,
	"Team 2" : 0,
	"Team 3" : 0,
	"Team 4" : 0,
	"User Team" : 0
	}

TotalPasses = {
	"Team 1" : 0,
	"Team 2" : 0,
	"Team 3" : 0,
	"Team 4" : 0,
	"User Team" : 0
	}


ScorersTable = {}

AssistsTable = {}

TeamGoals = {
	"Team 1" : 0,
	"Team 2" : 0,
	"Team 3" : 0,
	"Team 4" : 0,
	"User Team" : 0
	}

TeamAssists = {
	"Team 1" : 0,
	"Team 2" : 0,
	"Team 3" : 0,
	"Team 4" : 0,
	"User Team" : 0
	}

NAMEPLACE = -13 #the index where the players name ends

###################################################################################
###################################TeamSheets######################################
###################################################################################

def TeamSheets(Team, TeamList, numPlayers):

  """
  This function generates team sheets of 11 players for a match. 
  Each entry is formatted as <full name> <position> <rating> for the Game function below.

  Preconditions:
  Team: list with length numPlayers
  TeamList: Empty list
  numPlayers: integer > 0

  Parameters: 
  Team: The team that the team sheet is being generated for
  TeamList: The list that the sheet is being generated in
  numPlayers: number of players in a team 

	Returns:
	TeamList: A list with 11 different names
	"""
  x = 0


  for i in range(3): #Attackers

    x = 0
    TeamList.append(Team[(r.randint(0, int(numPlayers * 1/3) - 2))]) #adds a random name from Team(x) to the team sheet that is being generated

    if (TeamList[-1] in TeamList[:-1]) and i > 0: #checks if the last name added had already been added to hthe team sheet
      while x == 0: #continues to remove and add names unitil a name is added which is not a duplicate

        TeamList.pop(-1)
        TeamList.append(Team[(r.randint(0, int(numPlayers * 1/3) - 2))])
        if (TeamList[-1] in TeamList[:-1]) == False:
          x = x + 1

  
  for i in range (3): #Midfielders

    x = 0
    TeamList.append(Team[(r.randint(int(numPlayers * (1/3)), int((numPlayers * (2/3) - 1))))])
    
    if (TeamList[-1] in TeamList[:-1]) and i > 0:
      while x == 0:
        
        TeamList.pop(-1)
        TeamList.append(Team[(r.randint(int(numPlayers * (1/3)), int(numPlayers * (2/3) - 1)))])
        
        if (TeamList[-1] in TeamList[:-1]) == False:
          x = x + 1	
  
  
  for i in range(4): #Defenders
    
    x = 0
    TeamList.append(Team[(r.randint(int(numPlayers * (2/3)), numPlayers))])
    
    if (TeamList[-1] in TeamList[:-1]) and i > 0:
      while x == 0:
        
        TeamList.pop(-1)
        TeamList.append(Team[(r.randint(int(numPlayers * (2/3)), numPlayers))])
        
        if (TeamList[-1] in TeamList[:-1]) == False:
          x = x + 1

  TeamList.append(Team[(numPlayers + 1)]) #Goalkeeper

  return TeamList

###################################################################################
####################################SheetListing###################################
###################################################################################

def UserTeamsheet (TeamList, picked):
	"""
	This function lets the user pick their own team for a game instead of having the team picked for them randomly.

	Preconditions:
	TeamList: List with length Generation.n (number of players in each team)
	Picked: Empty list

	Postconditions:
	TeamList: all the pickable players
	Picked: the players the user picks are stored in this list

	Returns:
	nothing
	"""

	count = 1
	AllPlayers = []
	picker = str()
	pickerInt = int()
	stage = 3 #number of players need to move onto the next selection stage

	positions = ["Attackers", "Midfielders" ,"Defenders"]

	print ("")
	print ("Choose your Team")

	for i in range(2):

		print ("Choose 3 " + positions[i] + ":")

		for name in TeamList: #adding the all names from the users team to AllPlayers with the position removed
			if name[-11:-3] == positions[i][:8]:
				print (str(count) + ": " + name)
				count = count + 1
				AllPlayers.append(name)

		print ("Enter the number of the player who you would like to pick: ")

		while len(picked) < stage:
			picker = (input())

			try:
				
				pickerInt = int(picker) - 1

				if pickerInt > len(AllPlayers) or pickerInt < 0:
					print ("Please enter a valid number")
					print ("Pick next player:")

				else:
					if AllPlayers[pickerInt] not in picked:
						picked.append(AllPlayers[pickerInt])
						print ("Player added")
						if len(picked) < stage:
							print ("Pick next player:")

					else:
						print ("That player has been chosen already")
						print ("Pick next player:")

			except:
				print ("Please enter a valid number")
				print ("Pick next player:")

		stage = stage + 3
		AllPlayers.clear()
		count = 1
		print ("")



	print ("Choose 4 Defenders:")

	for name in TeamList:
		if name[-11:-3] == "Defender":
			print (str(count) + ": " + name)
			count = count + 1
			AllPlayers.append(name)

	print ("Enter the number of the player who you would like to pick: ")

	while len(picked) < 10:
		picker = (input())

		try:
				
			pickerInt = int(picker) - 1
			if pickerInt > len(AllPlayers) or pickerInt < 0:
				print ("Please enter a valid number")
				print ("Pick next player:")
					
			else:
				if AllPlayers[pickerInt] not in picked:
					picked.append(AllPlayers[pickerInt])
					print ("Player added")

					if len(picked) < stage + 1:
						print ("Pick next player:")
					
				else:
					print ("That player has been chosen already")
					print ("Pick next player:")
					
		except:
			print ("Please enter a valid number")
			print ("Pick next player:")

	AllPlayers.clear()
	count = 1

	picked.append(TeamList[-1])

	print ("")

	return picked



###################################################################################
####################################SheetListing###################################
###################################################################################

def SheetListing(Team1, Team2):
	"""
	This function takes 2 team sheets (generated with the TeamSheets function above) and 
	list them in an easy to read way.
	
	Preconditions:
	Team1: List with length 11
	Team2: List with length 11

	Postconditions:
	Team1: The team sheet for a team
	Team2: The teams sheet for a team

	Returns:
	Prints 23 lines with players from both teams on it
	"""

	NUMPLAYERS = 11 #number of players in a team

	if Team1 == TeamSheet1:
		HomeTeam = "Team 1"

	elif Team1 == TeamSheet2:
		HomeTeam = "Team 2"

	elif Team1 == TeamSheet3:
		HomeTeam = "Team 3"

	elif Team1 == TeamSheet4:
		HomeTeam = "Team 4"

	else:
		HomeTeam = "User Team"


	if Team2 == TeamSheet1:
		AwayTeam = "Team 1"

	elif Team2 == TeamSheet2:
		AwayTeam = "Team 2"

	elif Team2 == TeamSheet3:
		AwayTeam = "Team 3"

	elif Team2 == TeamSheet4:
		AwayTeam = "Team 4"

	elif Team2 == UserTeam:
		AwayTeam = "User Team"

	print ("Team Sheets:")

	print (HomeTeam)
	for i in range(NUMPLAYERS):
		print (Team1[i])

	print ("")

	print (AwayTeam)
	for i in range(NUMPLAYERS):
		print (Team2[i])

	print ("")
	input ("Press enter to start the game")

###################################################################################
################################TeamAverages#######################################
###################################################################################

def TeamAverages(Team1, Team2):
	"""
	This function takes both team sheets and finds the average of both teams attack,
	midfield and defence

	Preconditons:
	Team1: list with a length of 11
	Team2: list with a length of 11

	Postconditions:
	Team1: a team sheet generated with the TeamSheets function
	Team2: a team sheet generated with the TeamSheets function

	Returns:
	AverageAttack1: the average rating of the attackers for team1
	AverageAttack2: the average rating of the attackers for team2
  AverageMidfild1: the average rating of the midfielders for team1
  AverageMidfild2: the average rating of the midfielders for team2
	AverageDefence1: the average rating of the defendfers for team1
  AverageDefence2: the average rating of the defendfers for team2
	"""

	NUMPLAYERS = 11
	NUMATTACKERS = 3
	NUMMIDFIELDERS = 3
	NUMDEFENDERS = 4

	RATINGINDEX = -2

	AverageRating1 = 0
	AverageRating2 = 0
	
	AverageAttack1 = 0
	AverageAttack2 = 0

	AverageMidfield1 = 0
	AverageMidfield2 = 0

	AverageDefence1 = 0
	AverageDefence2 = 0

	for i in range (NUMPLAYERS):
		AverageRating1 = AverageRating1 + int(((Team1[i])[RATINGINDEX:]))
		AverageRating2 = AverageRating2 + int(((Team2[i])[RATINGINDEX:]))
	AverageRating1 = AverageRating1 / NUMPLAYERS
	AverageRating2 = AverageRating2 / NUMPLAYERS

	for i in range(NUMATTACKERS):
		AverageAttack1 = AverageAttack1 + int(((Team1[i])[RATINGINDEX:]))
		AverageAttack2 = AverageAttack2 + int(((Team2[i])[RATINGINDEX:]))
	AverageAttack1 = AverageAttack1 / NUMATTACKERS
	AverageAttack2 = AverageAttack2 / NUMATTACKERS

	for i in range(3,6):
		AverageMidfield1 = AverageMidfield1 + int(((Team1[i])[RATINGINDEX:]))
		AverageMidfield2 = AverageMidfield2 + int(((Team2[i])[RATINGINDEX:]))
	AverageMidfield1 = AverageMidfield1 / NUMATTACKERS
	AverageMidfield2 = AverageMidfield2 / NUMATTACKERS

	for i in range(6,10):
		AverageDefence1 = AverageDefence1 + int(((Team1[i])[RATINGINDEX:]))
		AverageDefence2 = AverageDefence2 + int(((Team2[i])[RATINGINDEX:]))
	AverageDefence1 = AverageDefence1 / NUMDEFENDERS
	AverageDefence2 = AverageDefence2 / NUMDEFENDERS

	return AverageAttack1, AverageAttack2, AverageMidfield1, AverageMidfield2, AverageDefence1, AverageDefence2, AverageRating1, AverageRating2


###################################################################################
####################################ScorerStats####################################
###################################################################################


def ScorerStats(PlayerName):
	"""
	This function puts players names into the ScorersTable dictionary.
	If the player has already scored, one is added to that players goals.
	If the player hasn't scored, their name is added as well as one goal

	Preconditions:
	PlayerName: string

	Postconditions:
	PlayerName: The name of the player who scored 

	Returns:
	Nothing
	"""
	PlayerName = PlayerName[:NAMEPLACE]
	GOALSADDED = 1

	if PlayerName in ScorersTable:
		ScorersTable[PlayerName] = ScorersTable[PlayerName] + GOALSADDED

	else:
		ScorersTable.update({PlayerName : GOALSADDED})


###################################################################################
#################################AssistStats#######################################
###################################################################################

def AssistStats(PlayerName):
	"""
	This function puts players names into the ScorersTable dictionary.
	If the player has already scored, one is added to that players goals.
	If the player hasn't scored, their name is added as well as one goal

	Preconditions:
	PlayerName: string

	Postconditions:
	PlayerName: The name of the player who scored 

	Returns:
	Nothing
	"""
	PlayerName = PlayerName[:NAMEPLACE]
	ASSITSADDED = 1

	if PlayerName in AssistsTable:
		AssistsTable[PlayerName] = AssistsTable[PlayerName] + ASSITSADDED

	else:
		AssistsTable.update({PlayerName : ASSITSADDED})


###################################################################################
############################*****!!!!!GAME!!!!!*****###############################
###################################################################################

def Game(Team1, Team2, delay = 0.2):
	"""
	This function is used to run a game. The game lasts for 90 'minutes' and can
	end in a win or a draw.

	Preconditions:
	Team1: list with length 11
	Team2: list with length 11

	Postconditions: 
	Team1: a team sheet generated with the TeamSheets function
	Team2: a team sheet generated with the TeamSheets function
	"""
	AvAtt1 = TeamAverages(Team1, Team2)[0]  #Getting the averages for the teams
	AvAtt2 = TeamAverages(Team1, Team2)[1]
	AvMid1 = TeamAverages(Team1, Team2)[2]
	AvMid2 = TeamAverages(Team1, Team2)[3]
	AvDef1 = TeamAverages(Team1, Team2)[4]
	AvDef2 = TeamAverages(Team1, Team2)[5]
	AvRating1 = TeamAverages(Team1, Team2)[6]
	AvRating2 = TeamAverages(Team1, Team2)[7]
	EventImportance = int() #important, major, minor, none
	EventType = int() #what type of event will be run

	distanceFromGoal = int() #how far away from goal a shot is
	ang = float() #angle of the header towards goal (only for corner)
	xG = float() #expected amount of goals from any given shot (can be thought of as a percentage chance that the player will score)
	#used equations found on https://cricketsavant.wordpress.com/2017/01/21/a-simple-expected-goals-model/ and data from
	#https://www.washingtonpost.com/news/fancy-stats/wp/2014/06/17/what-is-a-corner-kick-worth-in-soccer/
	#to calculate value

	PlayerPicker = int() #which position (Attack, midfield, defence) is picked for a senario
	PlayerPicker2 = int() #which position (Attack, midfield, defence) is picked for a senario
	PlayerName = str() #which player is picked for a senario (based on PlayerPicker)
	PlayerName2 = str() #which player is picked for a senario (based on PlayerPicker2)

	Team1Goals = 0 #how many goals Team1 has scored
	Team2Goals = 0 #how many goals Team2 has scored
	Team1Passes = 0 #how many passes Team1 has
	Team2Passes = 0 #how many passes Team2 has

	Team1_lowerBound = int()
	Team1_upperBound = int()

	Team2_lowerBound = int()
	Team2_upperBound = int()

	HomeTeam = str()
	AwayTeam = str()

	if Team1 == TeamSheet1:
		HomeTeam = "Team 1"

	elif Team1 == TeamSheet2:
		HomeTeam = "Team 2"

	elif Team1 == TeamSheet3:
		HomeTeam = "Team 3"

	elif Team1 == TeamSheet4:
		HomeTeam = "Team 4"

	else:
		HomeTeam = "User Team"


	if Team2 == TeamSheet1:
		AwayTeam = "Team 1"

	elif Team2 == TeamSheet2:
		AwayTeam = "Team 2"

	elif Team2 == TeamSheet3:
		AwayTeam = "Team 3"

	elif Team2 == TeamSheet4:
		AwayTeam = "Team 4"

	elif Team2 == UserTeam:
		AwayTeam = "User Team"


	for i in range(0, 90):
		t.sleep(delay)
		EventImportance = r.randint(0, 100)

		if EventImportance > 80:
			EventType = r.randint(1, 4) #shot close to goal, big mistake, penalty, freekick

			############################################################################
			#############################shot close to goal#############################
			############################################################################

			if EventType == 1:
				if r.randint(0, math.floor(AvAtt1 + AvAtt2 + AvMid1 + AvMid2)) <= AvAtt1 + AvMid2: 
					#this is choosing which Team the shot close to goal is for 
					#(The better attacking team will have a higher chance of getting the shot)

					PlayerPicker = r.randint(0,9) #picking what player will score/miss
					if PlayerPicker <= 6:
						PlayerName = Team1[r.randint(0,2)]
					elif PlayerPicker >= 8:
						PlayerName = Team1[r.randint(4, 5)]
					else:
						PlayerName = Team1[r.randint(6, 9)]

					distanceFromGoal = r.randint(0, 18) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)

					if 100 * xG > r.randint(0, 100):

							Team1Goals = Team1Goals + 1
							num1 = r.randint(0,9)
							num2 = r.randint(0,6)
							num3 = r.randint(0,3)
							
							adj = (CommentatorWords["Descript"][num1])
							tec = (CommentatorWords["type"][num2])
							are = (CommentatorWords["area"][num3])	

							print (str(i) + "'", PlayerName[:NAMEPLACE] ,"scores scores an " + adj + tec + "into the " + are + "from " + str(distanceFromGoal) + " yards out")
							ScorerStats(PlayerName)

					else:
						print (str(i) + "'", PlayerName[:NAMEPLACE], "missed the shot from", distanceFromGoal, "yards out")
												
				else: 

					PlayerPicker = r.randint(0,9) #picking what player will score/miss
					if PlayerPicker <= 6:
						PlayerName = Team2[r.randint(0,2)]
					elif PlayerPicker >= 8:
						PlayerName = Team2[r.randint(4, 5)]
					else:
						PlayerName = Team2[r.randint(6, 9)]

					distanceFromGoal = r.randint(0, 18) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)
					if 100 * xG > r.randint(0, 100):

							Team2Goals = Team2Goals + 1
								
							num1 = r.randint(0,9)
							num2 = r.randint(0,6)
							num3 = r.randint(0,3)
							
							adj = (CommentatorWords["Descript"][num1])
							tec = (CommentatorWords["type"][num2])
							are = (CommentatorWords["area"][num3])	

							print (str(i) + "'", PlayerName[:NAMEPLACE] ,"scores scores an " + adj + tec + "into the " + are + "from " + str(distanceFromGoal) + " yards out")

							ScorerStats(PlayerName)

					else:
						print (str(i) + "'", PlayerName[:NAMEPLACE],  "missed the shot from", distanceFromGoal, "yards out")

			############################################################################
			###############################big mistake##################################
			############################################################################

			elif EventType == 2: #mistake
				if r.randint(0, math.floor(AvDef1 + AvDef2)) <= AvDef2:

					PlayerPicker = r.randint(0,9) #picking what player will score/miss

					if PlayerPicker <= 6:
						PlayerName = Team1[r.randint(0,2)]
					elif PlayerPicker >= 8:
						PlayerName = Team1[r.randint(3, 5)]
					else:
						PlayerName = Team1[r.randint(6, 9)]

					PlayerPicker2 = r.randint(0,9) #picking what player will make the mistake					
					if PlayerPicker2 <= 3:
						PlayerName2 = Team2[r.randint(3,5)]
					else:
						PlayerName2 = Team2[r.randint(6, 9)]

					distanceFromGoal = r.randint(8, 20) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)

					if 100 * xG > r.randint(0, 100):

							Team1Goals = Team1Goals + 1
								
							num1 = r.randint(0,9)
							num2 = r.randint(0,6)
							num3 = r.randint(0,3)
							
							adj = (CommentatorWords["Descript"][num1])
							tec = (CommentatorWords["type"][num2])
							are = (CommentatorWords["area"][num3])	

							print (str(i) + "'", PlayerName[:NAMEPLACE] ,"scores scores an " + adj + tec + "into the " + are + "from " + str(distanceFromGoal) + " yards out after a mistake from " + PlayerName2[:NAMEPLACE])

							ScorerStats(PlayerName)

					else:
						print (str(i) + "'", PlayerName[:NAMEPLACE],  "missed the shot from", distanceFromGoal, "yards out")

				else:
					PlayerPicker = r.randint(0,9) #picking what player will score/miss
					if PlayerPicker <= 6:
						PlayerName = Team2[r.randint(0,2)]
					elif PlayerPicker >= 8:
						PlayerName = Team2[r.randint(3, 5)]
					else:
						PlayerName = Team2[r.randint(6, 9)]

					PlayerPicker2 = r.randint(0,9) #picking what player will make the mistake					
					if PlayerPicker2 <= 3:
						PlayerName2 = Team1[r.randint(3,5)]
					else:
						PlayerName2 = Team1[r.randint(6, 9)]

					distanceFromGoal = r.randint(8, 20) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)
					if 100 * xG > r.randint(0, 100):

							Team2Goals = Team2Goals + 1
								
							num1 = r.randint(0,9)
							num2 = r.randint(0,6)
							num3 = r.randint(0,3)
							
							adj = (CommentatorWords["Descript"][num1])
							tec = (CommentatorWords["type"][num2])
							are = (CommentatorWords["area"][num3])	

							print (str(i) + "'", PlayerName[:NAMEPLACE] ,"scores scores an " + adj + tec + "into the " + are + "from " + str(distanceFromGoal) + " yards out after a mistake from " + PlayerName2[:NAMEPLACE])

							ScorerStats(PlayerName)
			
					else:
						print (str(i) + "'", PlayerName[:NAMEPLACE],  "missed the shot from", distanceFromGoal, "yards out")

			############################################################################
			#################################penalty####################################
			############################################################################

			elif EventType == 3:

				if r.randint(0,16) == 1:
					if r.randint(0, math.floor(AvRating1 + AvRating2)) <= AvRating1:

						PlayerPicker = r.randint(0,9) #picking what player will score/miss

						if PlayerPicker <= 6:
							index = r.randint(0,2)
							PlayerName = Team1[index]
							
						elif PlayerPicker >= 8:
							index = r.randint(3, 5)
							PlayerName = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team1[index]


						xG = (0.77 * (1.0025 ** int(PlayerName[-2:]))) ** int(Team2[-1][-2:])

						if 100 * xG > r.randint(0, 100):

							Team1Goals = Team1Goals + 1
							num1 = r.randint(0,9)
							adj = (CommentatorWords["Descript"][num1])
								
							print (str(i) + "'", PlayerName[:NAMEPLACE] ,"scores a" + adj + "penalty")

							ScorerStats(PlayerName)

						else:
							print (str(i) + "'", PlayerName[:NAMEPLACE], "how did he miss the penalty?")
				
					else:
						PlayerPicker = r.randint(0,9) #picking what player will score/miss

						if PlayerPicker <= 6:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						elif PlayerPicker >= 8:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						else:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						xG = (0.77 * (1.0025 ** int(PlayerName[-2:]))) ** int(Team1[-1][-2:])

						if 100 * xG > r.randint(0, 100):

							Team2Goals = Team2Goals + 1
								
							num1 = r.randint(0,9)
							adj = (CommentatorWords["Descript"][num1])
								
							print (str(i) + "'", PlayerName[:NAMEPLACE] ,"scores a" + adj + "penalty")

							ScorerStats(PlayerName)

						else:
							print (str(i) + "'", PlayerName[:NAMEPLACE], "how did he miss the penalty?")

			############################################################################
			###################################freekick#################################
			############################################################################

			else: 
				if r.randint(0,4) == 1:
					if r.randint(0, math.floor(AvMid1 + AvMid2)) <= AvMid1:
						
						PlayerPicker = r.randint(0,9) #picking what player will score/miss

						if PlayerPicker <= 6:
							index = r.randint(0,2)
							PlayerName = Team1[index]

						elif PlayerPicker >= 8:
							index = r.randint(3, 5)
							PlayerName = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team1[index]


						distanceFromGoal = r.randint(19, 30) #the closer the shot the higher the chance of scoring

						xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)

						if 100 * xG > r.randint(0, 100):

							Team1Goals = Team1Goals + 1

							num1 = r.randint(0,9)
							num2 = r.randint(0,3)
							adj = (CommentatorWords["Descript"][num1])
							are = (CommentatorWords["area"][num2])	
								
							print (str(i) + "'", PlayerName[:NAMEPLACE] ,"scores a " + adj + "freekick into the " + are)

							ScorerStats(PlayerName)

						else:
							print (str(i) + "'", PlayerName[:NAMEPLACE], "skied the freekick")
				
					else:
						PlayerPicker = r.randint(0,9) #picking what player will score/miss

						if PlayerPicker <= 6:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						elif PlayerPicker >= 8:
							index = r.randint(3, 5)
							PlayerName = Team2[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team2[index]

						distanceFromGoal = r.randint(19, 30) #the closer the shot the higher the chance of scoring

						xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1

						if 100 * xG > r.randint(0, 100):

							Team2Goals = Team2Goals + 1
							num1 = r.randint(0,9)
							num2 = r.randint(0,3)
							adj = (CommentatorWords["Descript"][num1])
							are = (CommentatorWords["area"][num2])	
								
							print (str(i) + "'", PlayerName[:NAMEPLACE] ,"scores a " + adj + "freekick into the " + are)

							ScorerStats(PlayerName)

						else:
							print (str(i) + "'", PlayerName[:NAMEPLACE], "skied the freekick")

		############################################################################
		#############################medium important event#########################
		############################################################################

		elif (EventImportance > 50):
			EventType = r.randint(1,3) #corner, through ball, longshot

			############################################################################
			#############################corner (header)################################
			############################################################################

			if EventType == 1 and r.randint(1,3) == 1: #corner

				if r.randint(0, math.floor(AvAtt1 + AvAtt2 + AvMid1 + AvMid2)) <= AvAtt1 + AvMid2: 

					if r.randint(0,100) < 17:
						while PlayerName == PlayerName2:
							PlayerPicker = r.randint(0,9) #picking what player will take corner

							if PlayerPicker <= 3:
								index = r.randint (0, 2)
								PlayerName = Team1[index]

							else:
								index = r.randint(3,5)
								PlayerName = Team1[index]

						PlayerPicker2 = r.randint(0,9) #picking what player will win the header

						if PlayerPicker2 <= 3:
							index = r.randint(3, 5)
							PlayerName2 = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName2 = Team1[index]

						ang = r.randint(1,60)

						xG = (0.0162 * ang - 0.0178) * (int(PlayerName[-2:]) / 100)

						if r.randint(0,100) < (100 * xG):
							Team1Goals = Team1Goals + 1

							print (str(i) + "'", PlayerName2[:NAMEPLACE], "scores a great header!")

							ScorerStats(PlayerName2)
							AssistStats(PlayerName)

						else:
							print (str(i) + "'", PlayerName2[:NAMEPLACE], "missed the header")
						
				else:
					while PlayerName == PlayerName2:
						PlayerPicker = r.randint(0,9) #picking what player will take corner
							
						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team2[index]
						else:
							index = r.randint(3, 5)
							PlayerName = Team2[index]

						PlayerPicker2 = r.randint(0,9) #picking what player will win the header

						if PlayerPicker2 <= 3:
							index = r.randint(3, 5)
							PlayerName2 = Team2[index]

						else:
							index = r.randint(6, 9)
							PlayerName2 = Team2[index]

						ang = r.randint(1,60)

						xG = (0.0162 * ang - 0.0178) * (int(PlayerName[-2:]) / 100)

						if r.randint(0,100) < (100 * xG):
							Team2Goals = Team2Goals + 1

							print (str(i) + "'", PlayerName2[:NAMEPLACE], "scores a great header!")

							ScorerStats(PlayerName2)
							AssistStats(PlayerName)

						else:
							print (str(i) + "'", PlayerName2[:NAMEPLACE], "missed the header")

			############################################################################
			###############################through ball#################################
			############################################################################

			elif EventType == 2: #through ball
				if r.randint(0, math.floor(AvAtt1 + AvAtt2 + AvMid1 + AvMid2)) <= AvAtt1 + AvMid2: 
					PlayerPicker = 0
					PlayerPicker2 = 0
					PlayerName = ""
					PlayerName2 = ""

					while PlayerName == PlayerName2:

						PlayerPicker = r.randint(0,9) #picking what player will play the pass
						PlayerPicker2 = r.randint(0, 9) #picking the player who will score

						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team1[index]

						elif PlayerPicker <= 8:
							index = r.randint(3, 5)
							PlayerName = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team1[index]

							###########################################

						if PlayerPicker2 <= 6:
							index = r.randint(0, 2)
							PlayerName2 = Team1[index]

						else:
							index = r.randint(3, 5)
							PlayerName2 = Team1[index]



					distanceFromGoal = r.randint(10, 20) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1

					if 100 * xG > r.randint(0, 100):

						Team1Goals = Team1Goals + 1

						num1 = r.randint(0, 9)
						num4 = r.randint(0, 9)
						num2 = r.randint(0, 6)
						num3 = r.randint(0, 3)

						adj = (CommentatorWords["Descript"][num1])
						adj2 = (CommentatorWords["Descript"][num4])
						tec = (CommentatorWords["type"][num2])
						are = (CommentatorWords["area"][num3])

						print (str(i) + "'", PlayerName2[:NAMEPLACE] ,"scores scores an " + adj + tec + "into the " + are + "after an " + adj2 + "pass from " + PlayerName[:NAMEPLACE])
						
						ScorerStats(PlayerName2)
						AssistStats(PlayerName)

					else:
						num1 = r.randint(0,9)
						adj = (CommentatorWords["Descript"][num1])
						
						print (str(i) + "'  " + PlayerName2[:NAMEPLACE] + " misses a big chance after a " + adj + "pass from "+ PlayerName[:NAMEPLACE])

				else:
					PlayerPicker = 0
					PlayerPicker2 = 0
					PlayerName = ""
					PlayerName2 = ""

					while PlayerName == PlayerName2:
						PlayerPicker = r.randint(0,9) #picking what player will play the pass
						PlayerPicker2 = r.randint(0, 9) #picking the player who will score

						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						elif PlayerPicker <= 8:
							index = r.randint(3, 5)
							PlayerName = Team2[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team2[index]

							###########################################
							
						if PlayerPicker2 <= 6:
							index = r.randint(0, 2)
							PlayerName2 = Team2[index]

						else:
							index = r.randint(3, 5)
							PlayerName2 = Team2[index]



					distanceFromGoal = r.randint(10, 20) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1

					if 100 * xG > r.randint(0, 100):

						Team2Goals = Team2Goals + 1

						num1 = r.randint(0, 9)
						num4 = r.randint(0, 9)
						num2 = r.randint(0, 6)
						num3 = r.randint(0, 3)

						adj = (CommentatorWords["Descript"][num1])
						adj2 = (CommentatorWords["Descript"][num4])
						tec = (CommentatorWords["type"][num2])
						are = (CommentatorWords["area"][num3])

						print (str(i) + "'", PlayerName2[:NAMEPLACE] ,"scores scores an " + adj + tec + "into the " + are + "after an " + adj2 + "pass from " + PlayerName[:NAMEPLACE])

						ScorerStats(PlayerName2)
						AssistStats(PlayerName)

					else:
						num1 = r.randint(0,9)
						adj = (CommentatorWords["Descript"][num1])

						print (str(i) + "'", PlayerName2[:NAMEPLACE], "misses a big chance after a " + adj + "pass from " + PlayerName[:NAMEPLACE])



			############################################################################
			################################Longshot####################################
			############################################################################

			elif EventType == 3 and r.randint(0,3) == 1: #longshot
				if r.randint(0, math.floor(AvAtt1 + AvAtt2 + AvMid1 + AvMid2)) <= AvAtt1 + AvMid2:

					PlayerPicker = 0
					PlayerPicker2 = 0
					PlayerName = ""
					PlayerName2 = ""

					while PlayerName == PlayerName2:

						PlayerPicker = r.randint(0,9) #picking what player will play the pass
						PlayerPicker2 = r.randint(0, 9) #picking the player who will score

						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team1[index]

						elif PlayerPicker <= 8:
							index = r.randint(3, 5)
							PlayerName = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team1[index]

							###########################################

						if PlayerPicker2 <= 3:
							index = r.randint(0, 2)
							PlayerName2 = Team1[index]

						else:
							index = r.randint(3, 5)
							PlayerName2 = Team1[index]



					distanceFromGoal = r.randint(18, 40) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1

					if 100 * xG > r.randint(0, 100):

						Team1Goals = Team1Goals + 1

						num1 = r.randint(0, 9)
						num2 = r.randint(0, 1)
						num3 = r.randint(0, 3)

						adj = (CommentatorWords["Descript"][num1])
						tec = (CommentatorWords["type"][num2])
						are = (CommentatorWords["area"][num3])

						print (str(i) + "'", PlayerName2[:NAMEPLACE] ,"scores scores an " + adj + tec + "into the " + are + "from " + str(distanceFromGoal) + " yards out")
						
						ScorerStats(PlayerName2)
						AssistStats(PlayerName)

					else:
						num1 = r.randint(0,9)
						adj = (CommentatorWords["Descript"][num1])
						
						print (str(i) + "'", PlayerName2[:NAMEPLACE], "misses a shot from " + str(distanceFromGoal) + " yards out")
						
						
						############################################################33

				else:
					PlayerPicker = 0
					PlayerPicker2 = 0
					PlayerName = ""
					PlayerName2 = ""

					while PlayerName == PlayerName2:

						PlayerPicker = r.randint(0,9) #picking what player will play the pass
						PlayerPicker2 = r.randint(0, 9) #picking the player who will score

						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						elif PlayerPicker <= 8:
							index = r.randint(3, 5)
							PlayerName = Team2[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team2[index]

							###########################################

						if PlayerPicker2 <= 3:
							index = r.randint(0, 2)
							PlayerName2 = Team2[index]

						else:
							index = r.randint(3, 5)
							PlayerName2 = Team2[index]



					distanceFromGoal = r.randint(18, 40) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1


					if 100 * xG > r.randint(0, 100):

						Team2Goals = Team1Goals + 1

						num1 = r.randint(0, 9)
						num2 = r.randint(0, 1)
						num3 = r.randint(0, 3)

						adj = (CommentatorWords["Descript"][num1])
						tec = (CommentatorWords["type"][num2])
						are = (CommentatorWords["area"][num3])

						print (str(i) + "'", PlayerName2[:NAMEPLACE] ,"scores scores an " + adj + tec + "into the " + are + "from " + str(distanceFromGoal) + " yards out")
						
						ScorerStats(PlayerName2)
						AssistStats(PlayerName)

					else:
						num1 = r.randint(0,9)
						adj = (CommentatorWords["Descript"][num1])
						
						print (str(i) + "'", PlayerName2[:NAMEPLACE], "misses a shot from " + str(distanceFromGoal) + " yards out")

			else:
				pass


		else:

			if i % 3 == 0:
				chance = r.randint(0,4)
				if chance == 0:
					print (str(i) + "' " + HomeTeam + " is passing the ball well")

				elif chance == 1:
					print (str(i) + "' " + AwayTeam + " is passing the ball well")

				else:
					pass

			Team1_lowerBound = 0.35 * (AvRating1 ** 0.37) + 1.72 #determines the lowerbound of passes made based on the average rating of the team
			Team2_lowerBound = 0.35 * (AvRating2 ** 0.37) + 1.72

			Team1_upperBound = 0.085 * AvRating1 + 6.6 #determines the upper bound of passes made based on the average rating of the team (I actually made these 2 lines on my own!)
			Team2_upperBound = 0.085 * AvRating2 + 6.6

			Team1Passes = Team1Passes + r.randint(int(Team1_lowerBound), int(Team1_upperBound))

			Team2Passes = Team2Passes + r.randint(int(Team2_lowerBound), int(Team2_upperBound))


	print ("        ", HomeTeam + ":", Team1Goals, "|", AwayTeam + ":", Team2Goals) #prints the final result
	print (HomeTeam, "Passes:", Team1Passes, "|", AwayTeam, "Passes:", Team2Passes)

	if Team1Goals == Team2Goals and Team1Goals > 0: #adds the correct number of points for each team based on the result. (win = 3, draw = 1, loss = 0)
		print ("An exciting game ends in a draw")
		LeagueTable[HomeTeam] = LeagueTable[HomeTeam] + 1
		LeagueTable[AwayTeam] = LeagueTable[AwayTeam] + 1

	elif Team1Goals == Team2Goals:
		print ("A drab game ends in a draw")
		LeagueTable[HomeTeam] = LeagueTable[HomeTeam] + 1
		LeagueTable[AwayTeam] = LeagueTable[AwayTeam] + 1

	elif (Team1Goals > Team2Goals):
		print(HomeTeam, "wins!")
		LeagueTable[HomeTeam] = LeagueTable[HomeTeam] + 3

	else:
		print(AwayTeam, "wins!")
		LeagueTable[AwayTeam] = LeagueTable[AwayTeam]  + 3

	TotalPasses[HomeTeam] = TotalPasses[HomeTeam] + Team1Passes
	TotalPasses[AwayTeam] = TotalPasses[AwayTeam] + Team2Passes


	print ("")



###################################################################################
############################*****!!!!!GAME!!!!!*****###############################
###################################################################################



def GameNoText(Team1, Team2):
	"""
	This function is used to run a game with no text. The game lasts for 90 'minutes' and can
	end in a win or a draw.

	Preconditions:
	Team1: list with length 11
	Team2: list with length 11

	Postconditions: 
	Team1: a team sheet generated with the TeamSheets function
	Team2: a team sheet generated with the TeamSheets function
	"""
	AvAtt1 = TeamAverages(Team1, Team2)[0]  #Getting the averages for the teams
	AvAtt2 = TeamAverages(Team1, Team2)[1]
	AvMid1 = TeamAverages(Team1, Team2)[2]
	AvMid2 = TeamAverages(Team1, Team2)[3]
	AvDef1 = TeamAverages(Team1, Team2)[4]
	AvDef2 = TeamAverages(Team1, Team2)[5]
	AvRating1 = TeamAverages(Team1, Team2)[6]
	AvRating2 = TeamAverages(Team1, Team2)[7]
	EventImportance = int() #important, major, minor, none
	EventType = int() #what type of event will be run

	distanceFromGoal = int() #how far away from goal a shot is
	ang = float() #angle of the header towards goal (only for corner)
	xG = float() #expected amount of goals from any given shot (can be thought of as a percentage chance that the player will score)

	PlayerPicker = int() #which position (Attack, midfield, defence) is picked for a senario
	PlayerPicker2 = int() #which position (Attack, midfield, defence) is picked for a senario
	PlayerName = str() #which player is picked for a senario (based on PlayerPicker)
	PlayerName2 = str() #which player is picked for a senario (based on PlayerPicker2)

	Team1Goals = 0 #how many goals Team1 has scored
	Team2Goals = 0 #how many goals Team2 has scored
	Team1Passes = 0 #how many passes Team1 has
	Team2Passes = 0 #how many passes Team2 has

	Team1_lowerBound = int()
	Team1_upperBound = int()

	Team2_lowerBound = int()
	Team2_upperBound = int()

	if Team1 == TeamSheet1:
		HomeTeam = "Team 1"

	elif Team1 == TeamSheet2:
		HomeTeam = "Team 2"

	elif Team1 == TeamSheet3:
		HomeTeam = "Team 3"

	elif Team1 == TeamSheet4:
		HomeTeam = "Team 4"

	else:
		HomeTeam = "User Team"


	if Team2 == TeamSheet1:
		AwayTeam = "Team 1"

	elif Team2 == TeamSheet2:
		AwayTeam = "Team 2"

	elif Team2 == TeamSheet3:
		AwayTeam = "Team 3"

	elif Team2 == TeamSheet4:
		AwayTeam = "Team 4"

	elif Team2 == UserTeam:
		AwayTeam = "User Team"

	for i in range(0, 90):
		EventImportance = r.randint(0, 100)

		if EventImportance > 80:
			EventType = r.randint(1, 4) #shot close to goal, big mistake, penalty, freekick

			############################################################################
			#############################shot close to goal#############################
			############################################################################

			if EventType == 1:
				if r.randint(0, math.floor(AvAtt1 + AvAtt2 + AvMid1 + AvMid2)) <= AvAtt1 + AvMid2: 
					#this is choosing which Team the shot close to goal is for 
					#(The better attacking team will have a higher chance of getting the shot)

					PlayerPicker = r.randint(0,9) #picking what player will score/miss
					if PlayerPicker <= 6:
						PlayerName = Team1[r.randint(0,2)]
					elif PlayerPicker >= 8:
						PlayerName = Team1[r.randint(4, 5)]
					else:
						PlayerName = Team1[r.randint(6, 9)]

					distanceFromGoal = r.randint(0, 18) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)

					if 100 * xG > r.randint(0, 100):

							Team1Goals = Team1Goals + 1
							ScorerStats(PlayerName)

					else:
						pass
												
				else: 

					PlayerPicker = r.randint(0,9) #picking what player will score/miss
					if PlayerPicker <= 6:
						PlayerName = Team2[r.randint(0,2)]
					elif PlayerPicker >= 8:
						PlayerName = Team2[r.randint(4, 5)]
					else:
						PlayerName = Team2[r.randint(6, 9)]

					distanceFromGoal = r.randint(0, 18) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)
					if 100 * xG > r.randint(0, 100):

							Team2Goals = Team2Goals + 1

							ScorerStats(PlayerName)

					else:
						pass

			############################################################################
			###############################big mistake##################################
			############################################################################

			elif EventType == 2: #mistake
				if r.randint(0, math.floor(AvDef1 + AvDef2)) <= AvDef2:

					PlayerPicker = r.randint(0,9) #picking what player will score/miss

					if PlayerPicker <= 6:
						PlayerName = Team1[r.randint(0,2)]
					elif PlayerPicker >= 8:
						PlayerName = Team1[r.randint(3, 5)]
					else:
						PlayerName = Team1[r.randint(6, 9)]

					PlayerPicker2 = r.randint(0,9) #picking what player will make the mistake					
					if PlayerPicker2 <= 3:
						PlayerName2 = Team2[r.randint(3,5)]
					else:
						PlayerName2 = Team2[r.randint(6, 9)]

					distanceFromGoal = r.randint(8, 20) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)

					if 100 * xG > r.randint(0, 100):

							Team1Goals = Team1Goals + 1

							ScorerStats(PlayerName)

					else:
						pass

				else:
					PlayerPicker = r.randint(0,9) #picking what player will score/miss
					if PlayerPicker <= 6:
						PlayerName = Team2[r.randint(0,2)]
					elif PlayerPicker >= 8:
						PlayerName = Team2[r.randint(3, 5)]
					else:
						PlayerName = Team2[r.randint(6, 9)]

					PlayerPicker2 = r.randint(0,9) #picking what player will make the mistake					
					if PlayerPicker2 <= 3:
						PlayerName2 = Team1[r.randint(3,5)]
					else:
						PlayerName2 = Team1[r.randint(6, 9)]

					distanceFromGoal = r.randint(8, 20) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)
					if 100 * xG > r.randint(0, 100):

							Team2Goals = Team2Goals + 1

							ScorerStats(PlayerName)
			
					else:
						pass

			############################################################################
			#################################penalty####################################
			############################################################################

			elif EventType == 3:

				if r.randint(0,16) == 1:
					if r.randint(0, math.floor(AvRating1 + AvRating2)) <= AvRating1:

						PlayerPicker = r.randint(0,9) #picking what player will score/miss

						if PlayerPicker <= 6:
							index = r.randint(0,2)
							PlayerName = Team1[index]
							
						elif PlayerPicker >= 8:
							index = r.randint(3, 5)
							PlayerName = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team1[index]


						xG = (0.77 * (1.0025 ** int(PlayerName[-2:]))) ** int(Team2[-1][-2:])

						if 100 * xG > r.randint(0, 100):

							Team1Goals = Team1Goals + 1

							ScorerStats(PlayerName)

						else:
							pass
				
					else:
						PlayerPicker = r.randint(0,9) #picking what player will score/miss

						if PlayerPicker <= 6:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						elif PlayerPicker >= 8:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						else:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						xG = (0.77 * (1.0025 ** int(PlayerName[-2:]))) ** int(Team1[-1][-2:])

						if 100 * xG > r.randint(0, 100):

							Team2Goals = Team2Goals + 1

							ScorerStats(PlayerName)

						else:
							pass

			############################################################################
			###################################freekick#################################
			############################################################################

			else: 
				if r.randint(0,4) == 1:
					if r.randint(0, math.floor(AvMid1 + AvMid2)) <= AvMid1:
						
						PlayerPicker = r.randint(0,9) #picking what player will score/miss

						if PlayerPicker <= 6:
							index = r.randint(0,2)
							PlayerName = Team1[index]

						elif PlayerPicker >= 8:
							index = r.randint(3, 5)
							PlayerName = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team1[index]


						distanceFromGoal = r.randint(19, 30) #the closer the shot the higher the chance of scoring

						xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100)

						if 100 * xG > r.randint(0, 100):

							Team1Goals = Team1Goals + 1

							ScorerStats(PlayerName)

						else:
							pass
				
					else:
						PlayerPicker = r.randint(0,9) #picking what player will score/miss

						if PlayerPicker <= 6:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						elif PlayerPicker >= 8:
							index = r.randint(3, 5)
							PlayerName = Team2[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team2[index]

						distanceFromGoal = r.randint(19, 30) #the closer the shot the higher the chance of scoring

						xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1

						if 100 * xG > r.randint(0, 100):

							Team2Goals = Team2Goals + 1

							ScorerStats(PlayerName)

						else:
							pass

		############################################################################
		#############################medium important event#########################
		############################################################################

		elif (EventImportance > 50):
			EventType = r.randint(1,3) #corner, through ball, longshot

			############################################################################
			#############################corner (header)################################
			############################################################################

			if EventType == 1 and r.randint(1,3) == 1: #corner

				if r.randint(0, math.floor(AvAtt1 + AvAtt2 + AvMid1 + AvMid2)) <= AvAtt1 + AvMid2: 

					if r.randint(0,100) < 17:
						while PlayerName == PlayerName2:
							PlayerPicker = r.randint(0,9) #picking what player will take corner

							if PlayerPicker <= 3:
								index = r.randint (0, 2)
								PlayerName = Team1[index]

							else:
								index = r.randint(3,5)
								PlayerName = Team1[index]

						PlayerPicker2 = r.randint(0,9) #picking what player will win the header

						if PlayerPicker2 <= 3:
							index = r.randint(3, 5)
							PlayerName2 = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName2 = Team1[index]

						ang = r.randint(1,60)

						xG = (0.0162 * ang - 0.0178) * (int(PlayerName[-2:]) / 100)

						if r.randint(0,100) < (100 * xG):
							Team1Goals = Team1Goals + 1

							ScorerStats(PlayerName2)
							AssistStats(PlayerName)

						else:
							pass
						
				else:
					while PlayerName == PlayerName2:
						PlayerPicker = r.randint(0,9) #picking what player will take corner
							
						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team2[index]
						else:
							index = r.randint(3, 5)
							PlayerName = Team2[index]

						PlayerPicker2 = r.randint(0,9) #picking what player will win the header

						if PlayerPicker2 <= 3:
							index = r.randint(3, 5)
							PlayerName2 = Team2[index]

						else:
							index = r.randint(6, 9)
							PlayerName2 = Team2[index]

						ang = r.randint(1,60)

						xG = (0.0162 * ang - 0.0178) * (int(PlayerName[-2:]) / 100)

						if r.randint(0,100) < (100 * xG):
							Team2Goals = Team2Goals + 1

							ScorerStats(PlayerName2)
							AssistStats(PlayerName)

						else:
							pass

			############################################################################
			###############################through ball#################################
			############################################################################

			elif EventType == 2: #through ball
				if r.randint(0, math.floor(AvAtt1 + AvAtt2 + AvMid1 + AvMid2)) <= AvAtt1 + AvMid2: 
					PlayerPicker = 0
					PlayerPicker2 = 0
					PlayerName = ""
					PlayerName2 = ""

					while PlayerName == PlayerName2:

						PlayerPicker = r.randint(0,9) #picking what player will play the pass
						PlayerPicker2 = r.randint(0, 9) #picking the player who will score

						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team1[index]

						elif PlayerPicker <= 8:
							index = r.randint(3, 5)
							PlayerName = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team1[index]

							###########################################

						if PlayerPicker2 <= 6:
							index = r.randint(0, 2)
							PlayerName2 = Team1[index]

						else:
							index = r.randint(3, 5)
							PlayerName2 = Team1[index]



					distanceFromGoal = r.randint(10, 20) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1

					if 100 * xG > r.randint(0, 100):

						Team1Goals = Team1Goals + 1
						
						ScorerStats(PlayerName2)
						AssistStats(PlayerName)

					else:
						pass


				else:
					PlayerPicker = 0
					PlayerPicker2 = 0
					PlayerName = ""
					PlayerName2 = ""

					while PlayerName == PlayerName2:
						PlayerPicker = r.randint(0,9) #picking what player will play the pass
						PlayerPicker2 = r.randint(0, 9) #picking the player who will score

						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						elif PlayerPicker <= 8:
							index = r.randint(3, 5)
							PlayerName = Team2[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team2[index]

							###########################################
							
						if PlayerPicker2 <= 6:
							index = r.randint(0, 2)
							PlayerName2 = Team2[index]

						else:
							index = r.randint(3, 5)
							PlayerName2 = Team2[index]



					distanceFromGoal = r.randint(10, 20) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1

					if 100 * xG > r.randint(0, 100):

						Team2Goals = Team2Goals + 1

						ScorerStats(PlayerName2)
						AssistStats(PlayerName)

					else:
						pass



			############################################################################
			################################Longshot####################################
			############################################################################

			elif EventType == 3 and r.randint(0,3) == 1: #longshot
				if r.randint(0, math.floor(AvAtt1 + AvAtt2 + AvMid1 + AvMid2)) <= AvAtt1 + AvMid2:

					PlayerPicker = 0
					PlayerPicker2 = 0
					PlayerName = ""
					PlayerName2 = ""

					while PlayerName == PlayerName2:

						PlayerPicker = r.randint(0,9) #picking what player will play the pass
						PlayerPicker2 = r.randint(0, 9) #picking the player who will score

						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team1[index]

						elif PlayerPicker <= 8:
							index = r.randint(3, 5)
							PlayerName = Team1[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team1[index]

							###########################################

						if PlayerPicker2 <= 3:
							index = r.randint(0, 2)
							PlayerName2 = Team1[index]

						else:
							index = r.randint(3, 5)
							PlayerName2 = Team1[index]



					distanceFromGoal = r.randint(18, 40) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1

					if 100 * xG > r.randint(0, 100):

						Team1Goals = Team1Goals + 1
						
						ScorerStats(PlayerName2)
						AssistStats(PlayerName)

					else:
						pass
						
						############################################################33

				else:
					PlayerPicker = 0
					PlayerPicker2 = 0
					PlayerName = ""
					PlayerName2 = ""

					while PlayerName == PlayerName2:

						PlayerPicker = r.randint(0,9) #picking what player will play the pass
						PlayerPicker2 = r.randint(0, 9) #picking the player who will score

						if PlayerPicker <= 3:
							index = r.randint(0, 2)
							PlayerName = Team2[index]

						elif PlayerPicker <= 8:
							index = r.randint(3, 5)
							PlayerName = Team2[index]

						else:
							index = r.randint(6, 9)
							PlayerName = Team2[index]

							###########################################

						if PlayerPicker2 <= 3:
							index = r.randint(0, 2)
							PlayerName2 = Team2[index]

						else:
							index = r.randint(3, 5)
							PlayerName2 = Team2[index]



					distanceFromGoal = r.randint(18, 40) #the closer the shot the higher the chance of scoring

					xG = (1.13 * math.e ** (-0.203 * distanceFromGoal) + 0.023) * (int(PlayerName[-2:]) / 100) #1


					if 100 * xG > r.randint(0, 100):

						Team2Goals = Team1Goals + 1
						
						ScorerStats(PlayerName2)
						AssistStats(PlayerName)

					else:
						pass

			else:
				pass


		else:

			Team1_lowerBound = 0.35 * (AvRating1 ** 0.37) + 1.72 #Same as above
			Team2_lowerBound = 0.35 * (AvRating2 ** 0.37) + 1.72

			Team1_upperBound = 0.085 * AvRating1 + 6.6
			Team2_upperBound = 0.085 * AvRating2 + 6.6

			Team1Passes = Team1Passes + r.randint(int(Team1_lowerBound), int(Team1_upperBound))

			Team2Passes = Team2Passes + r.randint(int(Team2_lowerBound), int(Team2_upperBound))


	print ("        ", HomeTeam + ":", Team1Goals, "|", AwayTeam + ":", Team2Goals)
	print (HomeTeam, "Passes:", Team1Passes, "|", AwayTeam, "Passes:", Team2Passes)
	if Team1Goals == Team2Goals and Team1Goals > 0:
		print ("An exciting game ends in a draw")
		LeagueTable[HomeTeam] = LeagueTable[HomeTeam] + 1
		LeagueTable[AwayTeam] = LeagueTable[AwayTeam] + 1

	elif Team1Goals == Team2Goals:
		print ("A drab game ends in a draw")
		LeagueTable[HomeTeam] = LeagueTable[HomeTeam] + 1
		LeagueTable[AwayTeam] = LeagueTable[AwayTeam] + 1

	elif (Team1Goals > Team2Goals):
		print(HomeTeam, "wins!")
		LeagueTable[HomeTeam] = LeagueTable[HomeTeam] + 3

	else:
		print(AwayTeam, "wins!")
		LeagueTable[AwayTeam] = LeagueTable[AwayTeam] + 3

	TotalPasses[HomeTeam] = TotalPasses[HomeTeam] + Team1Passes
	TotalPasses[AwayTeam] = TotalPasses[AwayTeam] + Team2Passes


	print ("")
 


def FullMatchDay (TeamA, TeamSheetA, TeamB, TeamSheetB, numPlayers, delay = 0.2):
	"""
	This function combines the TeamSheets, SheetListing and Game functions all together to fully simulate one game.

	Precondtions:
	TeamA: List with length numPlayers
	TeamB: List with Lenght numPlayers
	TeamSheetA: Empty list
	TeamSheetB: Empty list
	numPlayers: number > 0

	Postconditions:
	TeamA: all of the players for the "home team"
	TeamB: all of the players for the "away team"
	TeamSheetA: Where a teamsheet will be generated with the TeamSheets function
	TeamSheetB: Where a teamsheet will be generated with the TeamSheets function
	numPlayers: total number of players on a team 

	returns:
	nothing
	"""

	if TeamA != Generation.UserTeam: #if the user is playing, the function will use the UserTeamSheet function. Otherwise it will use the TeamSheet function
		TeamSheets(TeamA, TeamSheetA, numPlayers)


	else:
		UserTeamsheet(TeamA, TeamSheetA)


	if TeamB != Generation.UserTeam:
		TeamSheets(TeamB, TeamSheetB, numPlayers)


	else:
		UserTeamsheet(TeamB, TeamSheetB)


	if TeamSheetA == UserTeam or TeamSheetB == UserTeam:
		SheetListing(TeamSheetA, TeamSheetB)
		Game(TeamSheetA, TeamSheetB, delay)


	else:
		GameNoText(TeamSheetA, TeamSheetB)



