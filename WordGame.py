#!/usr/bin/env python3

'''
Shawn Arreguin
This is a remake of Wordle for practice
I'll try to redo it every now and then so I can track my improvment
9/18/24
'''




import random
Words = ["HANDS","GUESS","THUMB","PENCIL","GRASS","FLOWER","BRUTE","FIRES","FOUND","WASHI","DUCKS","BEARS","TOWEL","GRAPE","SOUND","EARTH","VENUS","CLOUD"]
Word = random.choice(Words)
Word_List = list(Word) #turns our chosen word into a list, makes it easier to cycle thru

Guesses=[]


attempt=0
print("The word is " +str(len(Word_List))+ " letters long. You have "+str(len(Word_List)+1)+" attempts.")

while attempt < len(Word_List)+1: #use a while loop to keep track of attempts
	
	print("Attempt "+ str(attempt+1) +": ", end="") #tells us to give an input, add one because python starts counting at 0 and ppl start counting at 1
	guess=input() 
	print("--------------------------")
	guess=guess.upper()
	Word_Guess = ["*"] * len(Word_List)
	
	if len(guess) == len(Word_List):
		Guesses.append(guess) #we append each of our guesses to a list so that we can keep track of them and let the user know what they have said
		
		if guess == Word: #if they guessed the word right
			print("YAY! You won!")
			print(Word_List)
			break

		else: #if they didn't, then several things happen. 
			
			for i in range(len(Word_List)): #1) these two for loops works like matrix navigation to match each letter in the guessed word to the actual word
				for j in range(len(guess)):
					
					if Word_List[i] == guess[j]: #does letter i of the word match letter j of the user's guess?
						#can we do this with a if x in y? -> that might be easier
						if i == j: #is letter i of the word in the same position as letter j of the user's guess?
							print("The letter ",guess[j], " is in the word at the same position!") #if so, let's tell them
							Word_Guess.pop(j) #let's get rid of the "*" that's in the position
							Word_Guess.insert(j,guess[j]) #let's place the letter there
						
						else: #the letter i of the word is in a different position as letter j of the user's guess
							if Word_Guess[j] == "*": #if we placed something, don't remove it -> i think this is the best thing to do, check for fringe scenarios
								print("The letter ",guess[j], " is in the word at a different position.") #tell the user
								Word_Guess.pop(j) #remove the "*"
								insert="~"+guess[j].lower()+"~" #this format tells the user that the word is not in the right situation
								Word_Guess.insert(j,insert) #place the letter in that position
							else:
								pass
					else:
						pass
		
		print(Word_Guess)
		mylist=[print(i) for i in Guesses] #list iteration prints all of our guesses, looks cleaner than for loop
		attempt+=1
	
	else:
		print("Word must be "+str(len(Word_List))+" letters long.")

print("--------------------------")
print("These were your guesses:")
mylist=[print(i) for i in Guesses]
print("The word was:",Word)






# while(Word_Guess.count("*") != 0):

# 	print("Current Standing: " + str(Word_Guess))
# 	for i in range(len(Word)):
# 		print("Input Letter " + str(i) + " : ",end="")
# 		Letter = input()

# 		if Letter == Word_List[i]:
# 			print("You got it!")
# 			Word_Guess[i] = Letter
# 		elif Letter in Word_List:
# 			print(Letter + " is in word, but not where you put it")
# 		else:
# 			print(Letter + " is not used")
# 		count+=1
# 		print("You've guessed :", count, " times.")

# print("You are correct, the word was: " + Word)

#Make this real WORDLE
#Each time you need to print your Guesses and highlight the letters that are correct but in the wrong place and highlight the ones that are correct that are in the right place



