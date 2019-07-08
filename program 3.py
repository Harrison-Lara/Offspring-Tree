########################################################################
##
## CS 101
## Program #3
## Name: Harrison Lara
## Email: hrlwwd@mail.umkc.edu
##
## PROBLEM : We need to create a goal string that needs to be matched through a
##           a mutation of 500 random strings and keep looping through this
##          till the goal string and fitness score is exact and the score is 0. 
##
## ALGORITHM : 
##  1. Random----------------- import random
##  2. Set the goal string (10-15 characters): ‘umkc kangaroos’
##  3. All strings have to be randomly generated
##  4. Population need to be set at 500------------------- population [500]
##  5. Each string in the population needs to be the same length as the goal
##      string
##  6. Create formula to find the fitness score of each string based on accuracy
##  7. Assign the formula to a variable
##  8. Put in a while loop and wait till it finds the exact goal string
##      Ord(value) – ord(value) of goal strings, iterate for each character
#       with absolute value
##  9. Print each string in the population with its fitness score, strings with
##      the lowest fitness score are better-----------
##    insert chr(random.randint(32,126))
##  10. Average all 500 scores and find the potential parent strings (parent
##      strings are higher than 300) 
##  11. The new offspring strings have a 1% chance of being mutated------------
##          if random.random() < 0.01:
##          do the 1% thing
##          else:
##          do the 99% thing
##  12. Take the two lowest and make them the parents, 50 50 chance to iterate
##  13. Iterate/start new population with previous strings to make a new
##      population of 500 kids
##  14. Breed those of the new population and reiterate till goal string found
##      using-------         population.append(item)
##  15. Create string and print out how many lines, cycles it took to find
##      goal string and print fitness score of 
##
## ERROR HANDLING:
##      None. 
##
## OTHER COMMENTS:
##      I have the program written to where it only outputs each mutated string as
##      it goes through the 500 and breeds. That way it is shorter and readable
##      without the mess of all 500 being shown and then looping through each time
##      to simplify.  
##
########################################################################

import random

##### FUNCTIONS #####
##function to generate a string to display to the user
def genPopulationString(myPop):
    pop = ""
    for item in myPop: ##loops through random list of characters
        pop += item ##add that character to my string
    return pop;

##calculate the fitness score
def calcFitScore(random, actual):
    score = 0
    index = 0
    for item in random:
        score += abs(ord(item) - ord(actual[index]))
        index += 1
    return score;

##print formatted string to the user
def printResults(random, score):
    output = ""
    output += 'Best fit so far: '
    output += genPopulationString(random)
    output += ' Score: '
    output += str(score)
    print (output)

##generate my population from a given breeding population
def genNewPopulation(breedingPop):
    smallPop = []
    indexA = random.randint(0, len(breedingPop) - 1)
    indexB = random.randint(0, len(breedingPop) - 1)
    while (indexA == indexB):
        indexB = random.randint(0, len(breedingPop) - 1)
    popA = breedingPop[indexA]
    popB = breedingPop[indexB]
    for i in range(0, len(popA)):        
        AorB = random.randint(0,1)
        
        ##do this if you got 0 for A or the breeding population is only 1
        if AorB == 0 or len(breedingPop) == 1:
            char = popA[i]
        else:
            char = popB[i]
        if random.random() < 0.01: ##mutate
            HorL = random.randint(0,1)
            if HorL == 0:
                char = chr(ord(char) - 1)
            else:
                char = chr(ord(char) + 1)
            smallPop.append(char)
        else: ##crossover
            smallPop.append(char)
            
    return smallPop;

def genRandomSmallPop(size):
    smallPop = []
    ##generate small population string
    for item in range(0, size):
        smallPop.append(chr(random.randint(32, 126)))

    return smallPop;

            
##### MAIN ##### 
##set correct population string
correctPop = "Kangaroos!"

population = []
##generate large population
for idx in range(0, 500):

    ##append the small pop to my large pop
    population.append(genRandomSmallPop(len(correctPop)))

print ('Starting population generated')

stop = False
while (stop == False):
    totalFitScore = 0
    listOfFitScores = []
    ##calculate the fitness score for a string
    for smallPop in population:
        fitScore = calcFitScore(smallPop, correctPop)
        listOfFitScores.append(fitScore)
        totalFitScore += fitScore

    ##calculate the average
    avg = float(totalFitScore)/len(population)

    smallestPop = listOfFitScores.index(min(listOfFitScores))
    if min(listOfFitScores) == 0:
        ##print min(listOfFitScores)
        stop = True

    ##print the best fit so far
    printResults(population[smallestPop], listOfFitScores[smallestPop])

    ##get rid of the bad fitness scores
    listOfIndexesToPop = []
    x = len(listOfFitScores) - 1
    for score in reversed(listOfFitScores):
        if score > avg:
            listOfIndexesToPop.append(x)
        x = x - 1

    for index in listOfIndexesToPop:
        population.pop(index)

    if len(population) <= 1:
        population.append(correctPop)

    ##get the new population
    newPop = []
    for i in range(0, 500):
        newPop.append(genNewPopulation(population))

    ##out with the old, in with the new
    population = newPop

