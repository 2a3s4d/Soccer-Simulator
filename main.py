import Generation
import MatchDay
import UserInfo
from os import system #this is to clear the screen after the starting screen


def SheetClear():
	"""
	This function clears all the team sheets.
	"""

	MatchDay.TeamSheet1 = list([])
	MatchDay.TeamSheet2 = list([])
	MatchDay.TeamSheet3 = list([])
	MatchDay.TeamSheet4 = list([])
	MatchDay.UserTeam = list([])



def displayLeagueTable():
	"""
	This function displays the LeagueTable dictionary from highest to lowest points. 
	"""
	
	num = 1

	Table_Order = sorted(MatchDay.LeagueTable.items(), key=lambda x: x[1], reverse=True) #https://careerkarma.com/blog/python-sort-a-dictionary-by-value/
	#all lines which look like this are all from the same source
	#it takes the all the items, lambda is a samll function wich returns 1 value, then reverses the list
	print ("")
	print ("League Table:")
	for team in Table_Order:
		print(str(num) + ": " + team[0] + ":", team[1]) #prints the top scorers from most to least goals
		num += 1
	print("")



def displayTopScorers():
	"""
	This function displays the ScorersTable dictionary from highest to lowest points. 
	"""

	Player_Order = sorted(MatchDay.ScorersTable.items(), key=lambda x: x[1], reverse=True)
	print ("")
	print ("Top Scorers:")
	for player in Player_Order:
		print(player[0], player[1]) 
	print ("")



def displayTopAssisters():
	"""
	This function displays the AssistsTable dictionary from highest to lowest points. 
	"""

	Player_Order = sorted(MatchDay.AssistsTable.items(), key=lambda x: x[1], reverse=True)
	print ("")
	print ("Top Assisters:")
	for player in Player_Order:
		print(player[0], player[1])
	print ("")



def displayPasses():
	"""
	This function displays the TotalPasses dictionary from highest to lowest points. 
	"""
	num = 1

	Pass_Order = sorted(MatchDay.TotalPasses.items(), key=lambda x: x[1], reverse=True)
	print ("")
	print ("Passes Made by Each Team:")
	for team in Pass_Order:
		print(str(num) + ": " + team[0] + ":", team[1])
		num += 1
	print ("")



def menu():
	"""
	This function is the menu of the game where you can see the League table, top scorers,
	top assisters and the passing stats for all the teams. 
	"""

	end = 0
	iteration = 1
	while end == 0: # when the player enters 0, the loop and function will end
		if iteration == 1:
			print ("Enter 0 to continue")
			print ("Enter 1 to view league standings")
			print ("Enter 2 to view top scorers")
			print ("Enter 3 to view top assisters")
			print ("Enter 4 to view passing stats")
		choice = input("Enter choice: ")

		try: #if the player enters an int number then this code will be run
			choice = int(choice)
			if choice == 0:
				end = 1
			
			elif choice == 1:
				displayLeagueTable()
				iteration += 1 #this makes it so the instructiond dont appear after every input
			
			elif choice == 2:
				displayTopScorers()
				iteration += 1

			elif choice == 3:
				displayTopAssisters()
				iteration += 1

			elif choice == 4:
				displayPasses()
				iteration += 1

			else:
				print ("Please enter a valid number".upper())
				iteration += 1
		
		except: #if its another kind of data it runs this code
			print ("Please enter a valid number".upper())
			iteration += 1

Generation.n = 20 #number of players in the team - 1

Generation.TeamGen(Generation.n) #generating the teams

Generation.TeamFiles() #putting the lists of players into files



startscreen = open("Graphics/Startscreen.txt", "r") #opens a text file
print (startscreen.read()) #prints the whole text file
startscreen.close() #closes the file

input() #when the player hits enter the program will continue



clear = lambda: system('clear')

clear() #clears the screen



UserInfo.p1 = (UserInfo.Profile(input("Enter your name: "),UserInfo.getAge()))



inst = input("Enter 1 if you want to read the instructions for the game\notherwise press enter: ")
if inst == "1":
	clear()
	instFile = open("instructions.txt", "r") #opens a text file
	print (instFile.read()) #prints the whole text file
	instFile.close() #closes the file
	input()
	clear()

else:
	pass


print ("Press enter to simulate all non User Team games")
input()

#Games

#Team1's matches
MatchDay.FullMatchDay(Generation.Team1, MatchDay.TeamSheet1, Generation.Team2, MatchDay.TeamSheet2, Generation.n)

SheetClear()

MatchDay.FullMatchDay(Generation.Team1, MatchDay.TeamSheet1, Generation.Team3, MatchDay.TeamSheet3, Generation.n)

SheetClear()

MatchDay.FullMatchDay(Generation.Team1, MatchDay.TeamSheet1, Generation.Team4, MatchDay.TeamSheet4, Generation.n)

SheetClear()
#################################################################################################################
#Team2's matches
MatchDay.FullMatchDay(Generation.Team2, MatchDay.TeamSheet2, Generation.Team3, MatchDay.TeamSheet3, Generation.n)

SheetClear()

MatchDay.FullMatchDay(Generation.Team2, MatchDay.TeamSheet2, Generation.Team4, MatchDay.TeamSheet4, Generation.n)

SheetClear()
#################################################################################################################
#Team3's Matches
MatchDay.FullMatchDay(Generation.Team3, MatchDay.TeamSheet3, Generation.Team4, MatchDay.TeamSheet4, Generation.n)

SheetClear()
menu()
##################################################################################################################
#UserTeam's Matches
MatchDay.FullMatchDay(Generation.UserTeam, MatchDay.UserTeam, Generation.Team1, MatchDay.TeamSheet1, Generation.n)
SheetClear()
menu()

MatchDay.FullMatchDay(Generation.UserTeam, MatchDay.UserTeam, Generation.Team2, MatchDay.TeamSheet2, Generation.n)
SheetClear()
menu()

MatchDay.FullMatchDay(Generation.UserTeam, MatchDay.UserTeam, Generation.Team3, MatchDay.TeamSheet3, Generation.n)
SheetClear()
menu()

MatchDay.FullMatchDay(Generation.UserTeam, MatchDay.UserTeam, Generation.Team4, MatchDay.TeamSheet4, Generation.n)

SheetClear()
menu()

if MatchDay.LeagueTable["User Team"] > MatchDay.LeagueTable["Team 1"] and MatchDay.LeagueTable["User Team"] > MatchDay.LeagueTable["Team 2"] and MatchDay.LeagueTable["User Team"] > MatchDay.LeagueTable["Team 3"] and MatchDay.LeagueTable["User Team"] > MatchDay.LeagueTable["Team 4"]:

	clear() #clears the screen
	cup = open ("Graphics/Winner.txt", "r") #opens a text file
	print (cup.read()) #prints the whole text file
	cup.close() #closes the file

	print(UserInfo.p1)

else:
	print ("")
	print ("Too bad. Sadly, you didn't win the league")
	print ("")

menu()

print ("")
print ("Game over. Thanks for playing!".upper())