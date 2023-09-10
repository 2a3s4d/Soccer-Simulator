# Random Names Generator 
import random 
import math

Team1 = [] #where all the name of the players on the teams will be stored
Team2 = []
Team3 = []
Team4 = []
UserTeam = []

FirstNames = [] #A list of all the first names
LastNames = [] #A list of all the last names
FullNames = [] #A list of all the full names

n = int() #number of names generated

#This adds the list of names in the FirstNames text file
#to a list called FirstNames
with open ('Names//1.FirstNames.txt', 'r') as FN:  
    for line in FN:
        FirstNames.append(line) #putting all of the names from the FirstNames text file into the FirstNames list

#This adds the list of names in the LastNames text file
#to a list called LastNames
with open ('Names//1.LastNames.txt', 'r') as LN:  
    for line in LN:                   
        LastNames.append(line)  #putting all of the names from the Lastname text file into the LastNames list


def NameGen (numPlayers):  
    """
		This function generates some number of random names. 
		(These names are not region sensitive eg. a name like Vladimir Ding is possible)

		Precondtions:
		numPlayers: integer > 0

		Parameters: 
		numPlayers: This is the number of names that are generated

		Returns:
		A number of players names which are generated using a random first and last name 
    """

    with open ("Names//2.FullNames.txt", "w") as clear:
      clear.write("") #clears the full names list

    for i in range((numPlayers * 5) + 6):
      with open ("Names//2.FullNames.txt", "a") as FullN:
        FullN.write(FirstNames[random.randint(0,299)].replace("\n", " ") + LastNames[random.randint(0,299)].replace("\n", " ") + "\n") #writes random full names into the FullNames text file

###################################################################################
###################################################################################
###################################################################################

def rating():
	"""
	Geneates a number from 10 to 99 which will be used as the ratnig when teams are generated later.
	Precondtions:
	None
	Parameters:
	None
	Returns: a random number from 10 to 99 as a string
	"""
	rating = str(random.randint(10, 99)) #generates one rating from 10 to 99
	return rating 

###################################################################################
###################################################################################
###################################################################################

def pos (numPlayers, i):
	"""
	Positions will be assigned to players based on what line their name is on in the FullNames text file. 
  
	Precondtions:
	numPlayers: integer > 0
	i: integer >= 0 which increaces untill it is = to numPlayers

	Parameters:
	numPlayers: the number of players on each team
	i: the number of times which the loop has run (from 0 to numPlayers)

	Returns:
 	If 33% of numPlayers is > i then the function will return Attacker
	If 33% of numPlayers is <= i and 66% of numPlayers is > i then the function will return Midfield
	Otherwise (eg. if 66% numPlayers < i) then the function will return Defence
	"""
	#this mankes it so a third of the players are attackers, a third are midfielders and a third ard defenders 
	if math.floor(numPlayers * (1/3)) > i:
		return ("Attacker ")

	elif math.floor(numPlayers * (1/3)) <= i and math.floor(numPlayers * (2/3)) > i:
		return ("Midfield ")#This is not "Midfielders" becase then it would have a different number of charactors then attacker and defender

	else:
	    return ("Defender ")

###################################################################################
###################################################################################
###################################################################################

def TeamGen (numPlayers):
  
	"""
	This function generates five teams with a number of players and assignes them random
	ratings using the rating functions 

	Precondtions:
	numPlayers: integer > 0

	Parameters:
	numPlayers: the number of players on each team

	Returns: The names and ratings of players into dictionaries (Team1, Team2, Team3, Team4,Team5)
	"""

	x = 0

	NameGen(numPlayers)

	with open ('Names//2.FullNames.txt', 'r') as NL:  
		for line in NL:
			FullNames.append(line) # adds lines to list FullNames

	for i in range(0, numPlayers + 1):
		Team1.append(str(FullNames[x] + pos(numPlayers, i)).replace("\n", " ") + rating()) #adds positions and ratings to players
		x = x + 1
	Team1.append(str(FullNames[-5] + "Goalkeeper ").replace("\n", " ") + rating()) #adds a goal keeper to the team

	for i in range(0, numPlayers + 1):
		Team2.append(str(FullNames[x] + pos(numPlayers, i)).replace("\n", " ") + rating())
		x = x + 1
	Team2.append(str(FullNames[-4] + "Goalkeeper ").replace("\n", " ") + rating())

	for i in range(0, numPlayers + 1):
		Team3.append(str(FullNames[x] + pos(numPlayers, i)).replace("\n", " ") + rating())
		x = x + 1
	Team3.append(str(FullNames[-3] + "Goalkeeper ").replace("\n", " ") + rating())

	for i in range(0, numPlayers + 1):
		Team4.append(str(FullNames[x] + pos(numPlayers, i)).replace("\n", " ") + rating())
		x = x + 1
	Team4.append(str(FullNames[-2] + "Goalkeeper ").replace("\n", " ") + rating())

	for i in range(0, numPlayers + 1):
		UserTeam.append(str(FullNames[x] + pos(numPlayers, i)).replace("\n", " ") + rating())
		x = x + 1
	UserTeam.append(str(FullNames[-1] + "Goalkeeper ").replace("\n", " ") + rating())

###################################################################################
###################################################################################
###################################################################################

def TeamFiles():
	"""
	This function complete team lists, generated with "TeamGen", into files. 
	"""
	with open ('Teams//Team1.txt', 'w') as T1: 
		for i in range(0, n + 2):
			T1.write(Team1[i] + "\n") #puts the names in the Teams lists into files

	with open ('Teams//Team2.txt', 'w') as T2:
		for i in range(0,  n + 2):
			T2.write(Team2[i] + "\n")

	with open ('Teams//Team3.txt', 'w') as T3:
		for i in range(0,  n + 2):
			T3.write(Team3[i] + "\n")

	with open ('Teams//Team4.txt', 'w') as T4:
		for i in range(0,  n + 2):
			T4.write(Team4[i] + "\n")

	with open ('Teams//UserTeam.txt', 'w') as UT:
		for i in range(0,  n + 2):
			UT.write(UserTeam[i] + "\n")

