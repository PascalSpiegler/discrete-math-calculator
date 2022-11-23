
#Below, we define functions Negation, Conjunction, Disjunction, Implication, Biconditional, abbreviationToBool, and boolToAbbreviation

operators = ['∧', '∨', 'V', '→', '↔'] #Our list of permitted operators excluding negation
negation = ['¬']
truthValues = ['T', 'F']  #Our list of assigned truth values
variables = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P0'] #Our list of unassigned truth values (I am assuming less than or equal to 10 will be used)

def Conjunction(string_p, string_q):
    # Converting the string abbreviations to the appropriate booleans to facilitate computation:
    p = abbreviationToBool(string_p)
    q = abbreviationToBool(string_q)
    # Computing the conjunction:
    result = (p and q)
    return boolToAbbreviation(result)

def Negation(string_p):
    # Converting the string abbreviations to the appropriate booleans to facilitate computation:
    p = abbreviationToBool(string_p)
    # Computing the negation:
    result = (not p)
    return boolToAbbreviation(result)

def Disjunction(string_p, string_q):
    # Converting the string abbreviations to the appropriate booleans to facilitate computation:
    p = abbreviationToBool(string_p)
    q = abbreviationToBool(string_q)
    # Computing the disjunction:
    result = (p or q)
    return boolToAbbreviation(result)

def Implication(string_p,string_q):
    # Converting the string abbreviations to the appropriate booleans to facilitate computation:
    p = abbreviationToBool(string_p)
    q = abbreviationToBool(string_q)
    # Computing the implication:
    if p and not q:
        result = False
    else:
        result = True
    return boolToAbbreviation(result)

def Biconditional(string_p,string_q):
    # Converting the string abbreviations to the appropriate booleans to facilitate computation:
    p = abbreviationToBool(string_p)
    q = abbreviationToBool(string_q)
    # Computing the biconditional:
    if p == q:
        result = True
    else:
        result = False
    return boolToAbbreviation(result)

def abbreviationToBool(string):
    #If "T" we return boolean True, if "F" we return boolean False, and if something else, we return a string "Error"
    if (string == "T"):
        return True
    elif (string == "F"):
        return False
    else:
        return "Error"

def boolToAbbreviation(bool):
    #If True we return string "T", if False we return boolean "F", and if something else, we return a string "Error"
    if (bool == True):
        return "T"
    elif (bool == False):
        return "F"
    else:
        return "Error"

#END OF SECTION 1


#BEGINNING OF SECTION 2: INPUT CLEANUP AND INPUT VALIDITY CHECK FUNCTIONS:

#Below, we create a function to clean up the user input (remove spaces, replace 'TRUE' with 'T', replace 'FALSE' with 'F')
def cleanOriginalStatement(originalStatement):
    statement = originalStatement.replace("TRUE", "T") #We replace 'TRUE' with 'T' to faciliate computation later
    statement = statement.replace("FALSE", "F")  #We replace 'FALSE' with 'F' to faciliate computation later
    statement = statement.replace(" ", "") #We remove all the spaces from our string 
    return statement


#First, we create a function that checks whether only allowed characters were included in the user input:
def checkInputCharacters(statement):
    allowed = ['T', 'F', '(', ')', '¬', '∧', '∨', 'V', '→', '↔'] #These are the only characters allowed for the program
    for i in range(len(statement)-1): #We interate through every character in the statement
        if (statement[i] not in allowed): #If there is a character not in our list, we will print an error into console and return False
            print(statement[i] + " is an invalid input element.\nPlease only pick input elements from the following list and run the program again: " + str(allowed), " or ['P0', 'P1', ... , 'P9']")
            raise SystemExit(0)
    return True #If all characters respect our list, we will return True

#Next, we check if our parentheses are balanced:
def checkIfParenthesesValid(statement):
    parenthesesStack = [] #We create a 'stack' data structure using a list
    for character in statement: #We iterate through every character in our statement:
        if character == '(': #Whenever we encounter an open bracket, we append it to our stack:
            parenthesesStack.append(character)
        elif character == ')': #Whenever we encounter a closed bracket, we pop it from our stack if it matches the top element and our stack is not empty
            if (len(parenthesesStack) > 0) and (parenthesesStack[len(parenthesesStack)-1] == '('):
                parenthesesStack.pop()
            else: #If the the top element is not an open bracket or the stack is empty after a closed bracket encounter, the parentheses are not balanced:
                print("Unbalanced parentheses. Please make sure parentheses '(' and ')' are balanced and try again. \n") #In this case, we print an error 
                return False #We return false
    if len(parenthesesStack) == 0: #If by this line, we haven't returned anything and the size of the stack is empty, the parentheses are valid and we return True:
        return True
    else: #Else, the parentheses are not valid, so we print an error message and return False:
        print("Unbalanced parentheses. Please make sure parentheses '(' and ')' are balanced and try again. \n")
        return False


#This function will check whether there are NOT operators next to each other (i.e. P1 ∨ ∨ P2) or NOT two truth variables next to each other:
def checkInputValidArrangement(statement):

    if (statement[0] in operators): #If the first character in the statement is an operator, it is invalid (excluding negation operators)
        print("Invalid. Cannot have begin your statement with '" + statement[0] + "'.")
        return False

    if (statement[-1] in operators) or (statement[-1] in negation): #If the last character in the statement is an operator (including negation operators), it is invalid
        print("Invalid. Cannot have your statement end with '" + statement[-1] + "'.")
        return False

    for i in range(len(statement)-1): #Here, we iterate through every character in the statement except the last one
        #If the character and the next character equal each other, and are either in the operators or truthValues lists, the input is invalid (so we print an error and return False):
        if (statement[i] in operators and statement[i+1] in operators) or (statement[i] in truthValues and statement[i+1] in truthValues):
            print("Invalid. Cannot have " + statement[i] + " next to " + statement[i+1] + " in an expression. Please correct your input and try again.")
            return False

    for i in range(len(statement)-3): #Here, we iterate through every character in the statement except the last three
        #We scan all potential 2-character substrings, and check if they are in our unassigned variables list and equal the next 2-character substrings
        if (statement[i:i+2] in variables and statement[i+2:i+4] in variables): 
            #If true, we print an error message and return False  
            print("Invalid. Cannot have " + statement[i:i+2] + " next to " + statement[i+2:i+4] + " in an expression. Please separate them by an operator and try again.")
            return False

    #If no anomalies are found, the validity check returns as True
    return True

#Here, we make a function that checks whether the aforementioned validity checks (checkIfParenthesesValid, checkIfValidArrangement) are all true
def checkIfInputValid(statement):
    return checkIfParenthesesValid(statement) and checkInputValidArrangement(statement)


def checkReplacedInputValid(statement): #This function checks if the input is valid AFTER we replace all propositional variables with T or F:

    checkInputCharacters(statement) #We only want to call the checkInputCharacters() function after we have replaced our unassigned propositional variables

    #We iterate three characters at a time
    for i in range(len(statement)-3):
        #If the middle character is an operator (excluding negation):
        if (statement[i+1] in operators):
            #If the character before the operator isn't a truth value or a closing parenthesis, it is invalid:
            if ((statement[i] not in truthValues) and statement[i] != ')'):
                print("You cannot have " + statement[i] + " before an operator (except ¬). Please run program again with correct input.")
                raise SystemExit(0)
            #If the character after the operator isn't a truth value, an opening parenthesis, or a negation, it is invalid:
            if ((statement[i+2] not in truthValues) and (statement[i+2] != '(') and (statement[i+2] not in negation)):
                print("You cannot have " + statement[i] + " after an operator. Please run program again with correct input.")
                raise SystemExit(0)
        
        #If the middle character is a negation
        if (statement[i+1] in negation):
            #If the character before the negation isn't an operator or an opening parenthesis, it is invalid
            if ((statement[i] not in operators) and (statement[i] != '(') and (statement[i] not in negation)):
                print("You cannot have " + statement[i] + " before a negation. Please run program again with correct input.")
                raise SystemExit(0)
            #If the character after the negation isn't a truth value, an opening parenthesis, or another negation, it is invalid:
            if ((statement[i+2] not in truthValues) and (statement[i+2] != '(') and (statement[i+2] not in negation)):
                print("You cannot have " + statement[i] + " after a negation. Please run program again with correct input.")
                raise SystemExit(0)
        
        #If the middle character is a propositional variable:
        if (statement[i+1] in truthValues):
            #If the character before the propositional variable isn't an operator, opening parenthesis, or negation, it is invalid:
            if ((statement[i] not in operators) and (statement[i] != '(') and (statement[i] not in negation)):
                print("You cannot have " + statement[i] + " before a propositional variable. Please run program again with correct input.")
                raise SystemExit(0)
            #If the character after the propositional variable isn't an operator or closing parenthesis:
            if ((statement[i+2] not in operators) and statement[i+2] != ')'):
                print("You cannot have " + statement[i+2] + " after a propositional variable. Please run program again with correct input.")
                raise SystemExit(0)

#END OF SECTION 2 (INPUT CLEANUP AND INPUT VALIDITY FUNCTIONS)

# START OF SECTION 3 - PARSER AND SENTENCE COMPUTER
# The function below is used in both Q1 and Q2 to compute the final truth value of any given propositional setence.
# It will first simplify expressions within parentheses
# Then, once parentheses are handled, negations are applied
# Finally, Conjunction, Disjunction, Implications, and Biconditions are applied
# The parameters of this function is a logical statement (string), and whether or not we want steps to be shown (boolean). We will show steps in Q1's computation, but not Q2's.
def computeSentence(statement, showSteps):
    if len(statement) == 1 and statement[0] in truthValues: print(abbreviationToBool(statement)) #If we have one element in the sentence and it is a truth value, we can return its respective
    newString = "(" + str(statement) + ")" #We create a new string, which is a copy of the statement. We add parentheses around the whole statement to help us parse
    lastOpen = None #We initialize the lastOpen parenthesis variable to None
    lastClosed = None #We initialize the lastClosed parenthesis variable to None
    if showSteps == True: print("\nSteps:\n" + statement) #Here, if the showSteps parameter is toggled, we will show steps (Can be toggled to True when called in Q1)
    while len(newString) > 1: #We will iterate the contents of this while loop until we are left with 1 truth value (which will be our final answer)
        for i in range(len(statement)): #We will iterate through every character in our statement
            if '(' in statement: #If we encounter an open parenthesis, we set our lastOpen variable to the index of this parenthesis
                if statement[i] == '(':
                    lastOpen = i
                if statement[i] == ')': #If we encounter a closed parenthesis, we will compute the expression starting from the lastOpen parenthesis' position 
                    lastClosed = i 
                    substring = statement[lastOpen+1:lastClosed] #We generate a substring starting from lastOpen+1, ending at lastClosed (exclusive)       
                    if '¬' in substring: #If we have a negation operator, we will find its lastmost index (one at a time) and replace its subsequent truth variable with its negation:
                        index = substring.rfind('¬') #The rfind method finds the last instance of a character in a string and returns the index
                        if (substring[index+1] != '(' and substring[index+1] != '¬'): #We only run the negation of the subsequent variable if it is not another bracket or another negation
                            newString = newString.replace(substring[index:index+2], Negation(substring[index+1:index+2]))     #We change our newString variable, replacing ¬PX with its negation          
                            break
                    else: #If there are no negations left, then we will start computing our Conjunctions, Disjunctions, Implications, and Biconditionals

                        if (len(substring) == 1): #Edge case: If we have (T) or (F), we can replace this with just T or F:
                            newString = newString.replace(statement[lastOpen:lastClosed+1], substring)

                        if (len(substring) == 3): #If we are left with just 3 characters within our brackets, we can evaluate them (since all negations are handled)
                            if substring[1] == '∧': #If there is a conjunction operation, we replace the 3 characters with its result
                                newString = newString.replace(statement[lastOpen:lastClosed+1], Conjunction(substring[0], substring[2]))
                                break
                            elif substring[1] == '∨' or substring[1] == 'V': #If there is a disjunction operation, we replace the 3 characters with its result
                                newString = newString.replace(statement[lastOpen:lastClosed+1], Disjunction(substring[0], substring[2]))
                                break
                            elif substring[1] == '→': #If there is an implication operation, we replace the 3 characters with its result
                                newString = newString.replace(statement[lastOpen:lastClosed+1], Implication(substring[0], substring[2]))
                                break
                            elif substring[1] == '↔': #If there is a biconditional operation, we replace the 3 characters with its result
                                newString = newString.replace(statement[lastOpen:lastClosed+1], Biconditional(substring[0], substring[2]))
                                break
                        else : #This case will run when we still have things to compute within parentheses and there are >3 characters within our substring
                            for i in range(len(substring)): #We will iterate through the substring (contents of the parentheses)
                                if statement[i] == '¬': #If we find a negation operator, we replace it and its following character with its negation
                                    newString = newString.replace(statement[i:i+2], Negation(statement[i+1]))
                                    break
                                if '¬' not in substring: #Once we have handled all negations, we can move onto the other operations:
                                    #If we find a conjunction symbol, we replace the substring from its previous to its next variable with its result:
                                    if statement[i] == '∧':
                                        newString = newString.replace(statement[i-1:i+2], Conjunction(statement[i-1], statement[i+1]))
                                        break
                                    #If we find a disjunction symbol, we replace the substring from its previous to its next variable with its result:
                                    elif statement[i] == '∨' or statement[i] == 'V':
                                        newString = newString.replace(statement[i-1:i+2], Disjunction(statement[i-1], statement[i+1]))  
                                        break
                                    #If we find an implication symbol, we replace the substring from its previous to its next variable with its result:
                                    elif statement[i] == '→':
                                        newString = newString.replace(statement[i-1:i+2], Implication(statement[i-1], statement[i+1])) 
                                        break
                                    #If we find a biconditional symbol, we replace the substring from its previous to its next variable with its result:
                                    elif statement[i] == '↔':
                                        newString = newString.replace(statement[i-1:i+2], Biconditional(statement[i-1], statement[i+1]))    
                                        break 

        
            else: #If all parentheses have been handled
                #While iterating through every character of our statement, if we find a negation symbol, we replace it and its following character with its negation:
                if statement[i] == '¬': 
                    if (statement[i+1] != '(' and statement[i+1] != '¬'):
                        newString = newString.replace(statement[i:i+2], Negation(statement[i+1]))
                        break
                #If we find a conjunction symbol, we replace the substring from its previous to its next variable with its result:
                if statement[i] == '∧':
                    newString = newString.replace(statement[i-1:i+2], Conjunction(statement[i-1], statement[i+1]))
                    break
                #If we find a disjunction symbol, we replace the substring from its previous to its next variable with its result:
                elif statement[i] == '∨' or statement[i] == 'V':
                    newString = newString.replace(statement[i-1:i+2], Disjunction(statement[i-1], statement[i+1]))  
                    break
                #If we find an implication symbol, we replace the substring from its previous to its next variable with its result:
                elif statement[i] == '→':
                    newString = newString.replace(statement[i-1:i+2], Implication(statement[i-1], statement[i+1])) 
                    break
                #If we find a biconditional symbol, we replace the substring from its previous to its next variable with its result:
                elif statement[i] == '↔':
                    newString = newString.replace(statement[i-1:i+2], Biconditional(statement[i-1], statement[i+1]))    
                    break 
        
        
        if showSteps == True: print(newString) #If we want to show steps in our function (showSteps is True), we will print how the string is modified at every iteration
        statement = newString #We set our variable 'statement' to newString before we reiterate so we can keep shrinking our statement
    answer = abbreviationToBool(newString) #Once we have one truth variable remaining (while loop breaks), we set our final answer to equal newString
    if showSteps == True: print("Final Answer: ", end = "")
    print(answer) #We display our final answer
    return answer #We return our final answer

#END OF SECTION 3: PARSER AND SENTENCE COMPUTER

#START OF SECTION 4: PROGRAM 1

#The following function will scan the sentence entered by the user and create a dictionary of all unassigned propositional variables:
def populatePropDict(statement):
    propVarDict = {} #We create a dictionary which will hold any potential unassigned variables
    #We iterate through the statement and add any 2-character substring PX to our dictionary (X should be a series of numbers between 0-9)
    
    
    if len(statement) > 2: #If we have 3 or more characters in our sentence:
        for i in range(len(statement)-2): #We iterate through every character, excluding the last two
            if statement[i] == 'P' and statement[i+1].isdigit() and not statement[i+2].isdigit(): #If we find 'P' and the following character is a digit, and the character after that is not a digit:
                propVar = statement[i:i+2] #We can set the key of our propositional variable
                propVarDict[propVar] = None #We initially set value of the propositional variable to None
            elif not statement[i].isdigit() and statement[i+1] == 'P' and statement[i+2].isdigit(): #If we have 'P' as the second character of our iterating substring and there is no digit before it, but a digit after it:
                propVar = statement[i+1:i+3] #We can set the key of our propositional variable
                propVarDict[propVar] = None #We initially set value of the propositional variable to None
            elif statement[i] == 'P' and not statement[i+1].isdigit(): #If we have P but the subsequent character is not a digit, it is invalid
                print("Please run the program again and enter the propositional variables in the following format: P0, P1, P2, ... , P9")
                raise SystemExit(0)
            elif statement[i] == 'P' and statement[i+1].isdigit() and statement[i+2].isdigit(): #If we have P followed by a two digit integer, it is invalid (to simplify parsing I don't consider this case)
                print("Please run the program again and enter the propositional variables in the following format: P0, P1, P2, ... , P9")
                raise SystemExit(0)
    else: #If we only have one propositional variable (with the possibility of a negation before it)
        if (statement[0] not in negation): #If there is no negation
            if statement in variables: #If our two character substring is an unassigned variable
                propVar = statement #We can set the key of our propositional variable 
                propVarDict[propVar] = None #We initially set value of the propositional variable to None
            if (statement not in variables) and (statement not in truthValues): #If we don't have a propositional variable or a truth value remaining, it is invalid:
                print("Invalid. You cannot have a propositional sentence with only '" + statement + "'. Please run program again.")
                raise SystemExit(0)

    return propVarDict



#The function below represents the first question of the assignment
def program1():
    print("PROGRAM 1:")
    #We take input from the user and set it all to be upper case (for consistency)

    #We will keep asking the user for input until checkIfInputValid(statement) returns true (until they give a valid input)
    invalidInput = True
    while(invalidInput):    
        originalStatement = input("Please write a propositional sentence. \nExample: ((P1 ∧ P2) ∨ (P3 ∧ True)) ∨ ((¬P1 ∧ ¬P3) ∧ P2)\n").upper() 
        #This function will replace 'TRUE' with 'T', 'FALSE' with 'F', and remove all spaces    
        statement = cleanOriginalStatement(originalStatement) 
        if (checkIfInputValid(statement)): invalidInput = False 
    
    propVarDict = populatePropDict(statement) #We scan the sentence entered by the user and create a dictionary of all unassigned propositional variables:

    #Here, we iterate through the keys of our dictionary and allow the user to assign the truth variables:
    for key in propVarDict:
        invalidInput = True
        while invalidInput: #This will loop unless the user enters 'T' or 'F' as the assignment of their propositional variable(s)
            propVarDict[key] = input('What value would you like to set for ' + key + '? (T or F) \n').upper()
            if propVarDict[key] == 'T' or propVarDict[key] == 'F':
                invalidInput = False
            if invalidInput:
                print("Please try again and enter either 'T' or 'F' as the value of " + key)


    #Then, we modify the statement and swap our keys for the assigned truth variables:    
    for key, item in propVarDict.items():
        statement = statement.replace(key, item)

    #Once we have replaced the unassigned propositional variables with truth variables, we will call our validation function checkReplacedInputValid(statement)
    checkReplacedInputValid(statement)

    #If the user wishes to see the steps of the sentence computation, they can type T. If not, they can type F.
    showSteps = abbreviationToBool(input("Show steps? (T/F)\n").upper())

    #If the user wants to see additional information such as the original statement, they will have toggled showSteps
    if showSteps: print("Original statement:\n" + statement)
    
    #We run our computeSentence() method, sending our statement (string) and showSteps (boolean) as parameters. This will display our results.
    computeSentence(statement, showSteps)

#END OF SECTION 4: PROGRAM 1


#START OF SECTION 5: PROGRAM 2

#This function recursively generates all truth variable combinations for our propositional variables
def computeAllCombinations(num, propVars, statement, sentenceTruthValues = [], combinations=[]):
    #Base case: When num == 0
    if num == 0:
        #Here, we print out all combinations of our propositional variables and format it as a table
        for truthValue in combinations:
            print(boolToAbbreviation(truthValue) + "  |", end = "")

        #Here, we replace the statement's propositional variables with their respective truth variable combinations
        for i in range(len(propVars)):
            statement = statement.replace(propVars[i], boolToAbbreviation(combinations[i]))
        
        #For each combination of truth variables, we compute the sentence's final value
        result = computeSentence(statement, False)
        #We append the final value of each combination to a list, which we will return to determine if our table is a tautology, contingency, or contradiction
        sentenceTruthValues.append(result)

    else:
        #Recursive case: We keep calling computeAllCombinations(num-1, ...) until our base case of num == 0 so we end up with a nested loop with num nested loops (# of propositional variables):
        for truthValue in [True,False]:
            computeAllCombinations(num-1, propVars, statement, sentenceTruthValues, combinations+[truthValue])
    
    #We return our sentenceTruthValues to see if our table is a tautology, contingency, or contradiction
    return(sentenceTruthValues)

#Here, we check if our truth table values generate a tautology (always True):
def checkTautology(sentenceTruthValues):
    result = True #If there are no elements 'False' in our list, we have a tautology
    for i in range(len(sentenceTruthValues)): #We iterate through each truth value (for each combination)
        if sentenceTruthValues[i] == False: #If we find a single truth variable that is False, we do not have a tautology and return false
            result = False
    return result 

#Here, we check if our truth table values generate a contradiction (always False):
def checkContradiction(sentenceTruthValues):
    result = True #If there are no elements 'True' in our list, we have a tautology
    for i in range(len(sentenceTruthValues)): #We iterate through each truth value (for each combination)
        if sentenceTruthValues[i] == True: #If we find a single truth variable that is True, we do not have a contradiction and return false
            result = False
    return result

#Using our checkTautology and checkContadiction methods, we determine whether our truth table is a tautology, contradiction, or contingency:
def checkTruthTableType(sentenceTruthValues):
    if checkTautology(sentenceTruthValues):
        return "tautology"
    elif checkContradiction(sentenceTruthValues):
        return "contradiction"
    else: #By definition, if we neither have a tautology or a contradiction, we have a contingency
        return "contingency"


#The function below represents the second question of the assignment
def program2():
    print("PROGRAM 2:")
    propVars = [] #We create a list for our propositional variables
    
    invalidInput = True
    while(invalidInput):    
        originalStatement = input("Please write a propositional sentence. A truth table will be generated. \nExample: (¬P1 ∧ (P1 ∨ P2)) → P2\n").upper() 
        #This function will replace 'TRUE' with 'T', 'FALSE' with 'F', and remove all spaces    
        statement = cleanOriginalStatement(originalStatement) 
        if (checkIfInputValid(statement)): invalidInput = False 

    propVarDict = populatePropDict(statement) #We scan the sentence entered by the user and create a dictionary of all unassigned propositional variables:
    
    #To reuse the checkReplacedInputValid function from P1, we will create a dummy string where we replace all propositional variables with T (won't affect final result)

    dummyString = statement

    for key in propVarDict: #We push every key in our propVarDict to a list
        dummyString = dummyString.replace(key, 'T')

    #Now, we can do further input checks more simply:
    checkReplacedInputValid(dummyString)
    
    #If the dummyString (where variables are replaced with T) is valid, we can continue by pushing every key in our propVarDict to a list:
    for key in propVarDict:
        propVars.append(key)
    
    print("\nTruth table for " + originalStatement + ":\n")

    for propVar in propVars: #We will start formatting our truth table (column headers)
            print(propVar + " |", end = "")
    
    print(originalStatement) #We add the original statement as the last column of our truth table
    
    #We call our computeAllCombinations function, which recursively generates all truth variable combinations, then computes the final value of all these for our statement
    sentenceTruthValues = computeAllCombinations(len(propVars), propVars, statement)  
    
    #We determine whether our truth table is a tautology, contingency, or contradiction by calling our checkTruthTableType function
    truthTableType = (checkTruthTableType(sentenceTruthValues))

    #We print our final answer
    print(originalStatement + " is a " + truthTableType)

#END OF SECTION 5: PROGRAM 2


#START OF SECTION 6 (CHOOSING WHAT PROGRAMS TO RUN):
#Feel free to comment out whichever program you are not using. If left as is, each program will run after the other.

program1() 

program2()