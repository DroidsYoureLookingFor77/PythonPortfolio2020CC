#Connor Crowe
#12/11/2019

row0 = ("C","P","R","Q","T","U","I","Q","Y","L","U","E","O","Q","A","J","I","B","U","L")
row1 = ("D","W","R","U","Y","M","W","Y","R","L","T","C","F","Y","I","N","C","H","A","L")
row2 = ("V","I","P","I","P","J","K","O","N","A","E","U","N","I","T","N","O","C","X","P")
row3 = ("Y","N","Z","O","N","A","F","M","N","E","H","Q","Z","M","N","K","I","Q","B","N")
row4 = ("I","N","R","Z","C","T","N","E","G","L","Z","X","X","D","L","G","N","J","Z","L")
row5 = ("Y","T","C","W","L","A","T","Q","H","P","O","Z","I","T","O","T","Z","T","M","V")
row6 = ("C","U","P","E","J","A","I","D","C","U","F","E","U","L","E","D","V","M","C","P")
row7 = ("F","V","O","L","C","Z","X","Y","A","T","H","F","S","G","O","A","S","W","T","K")
row8 = ("X","Y","A","N","A","R","R","A","Y","O","C","W","E","N","A","F","O","H","Q","Z")
row9 = ("Y","L","O","R","I","W","G","S","P","R","O","G","R","A","M","M","Z","M","M","C")
row10 = ("F","C","A","Z","I","M","B","E","T","F","N","E","X","E","C","U","T","I","O","N")
row11 = ("U","N","J","N","L","A","R","N","Q","R","E","W","Z","L","L","F","Q","H","D","W")
row12 = ("N","F","S","T","I","A","B","R","Q","H","I","W","D","O","T","C","S","P","U","D")
row13 = ("C","L","Q","A","T","M","M","L","A","M","Z","N","G","O","S","A","A","A","L","J")
row14 = ("T","S","E","O","D","G","R","G","E","W","G","S","G","B","H","T","O","C","E","M")
row15 = ("I","J","R","Z","E","J","R","E","T","A","M","R","O","F","E","J","F","L","T","E")
row16 = ("O","D","G","X","D","L","J","Y","T","F","X","C","L","S","L","M","G","K","F","V")
row17 = ("N","K","U","G","H","K","A","I","C","G","B","N","P","P","L","Q","E","X","Y","V")
row18 = ("E","M","W","M","I","V","N","O","C","S","O","W","L","J","X","Y","W","F","H","K")
row19 = ("Z","O","M","H","A","T","J","T","T","L","Q","A","S","G","I","T","L","O","D","G")

words = ("Variable",
         "Float",
         "Function",
         "Tuple",
         "Input",
         "Operator",
         "Array",
         "Boolean",
         "String",
         "Print",
         "Module",
         "Import",
         "Shell",
         "Concatenate",
         "Logical",
         "Program",
         "Continue",
         "Format",
         "Terminal",
         "Execution")

questions = ("This is an object Python uses to store data. What is it?",
             "This is a number that has a decimal point and numbers following it. What is it?",
             "This is portion of code dedicated to the processing and output. What is it?",
             "This is a means of holding data that is pre-defined in code. What is it?",
             "This is a means of receiving data from a user. What is it?",
             "This is something Python uses to perform equations and compare. What is it?",
             "This is a mutable variable that stores sets of data of the same type. What is it?",
             "This is a data type that describes falsehood and truth. What is it?",
             "This is a data type that is used primarily to display data. What is it?",
             "This is an in-built function that allows users to display data to the screen. What is it?",
             "This is a part of Python that has to be manually imported for use. What is it?",
             "This is a function that allows Python to access libraries and modules. What is it?",
             "This is where Python programs run. What is it?",
             "This is the term for adding together multiple pieces of data. What is it?",
             "This is the term describing comparisons and operators. What is it?",
             "This is a file with code in it that can be executed in the shell. What is it?",
             "This is a command that can be inserted into a loop to make it keep going. What is it?",
             "This is a collection of rules that determine how Python code should be written and how it's read. What is it?",
             "This is an interface that Python and other programs use to display code and input commands. What is it?",
             "This is the term used to describe the running of a file. What is it?")

def randomQuestion(words, questions):
  import random
  rSelect = random.randint(0, len(words) - 1)
  rQuesUsed = []
  rWordUsed = []
  rQues = questions[rSelect]
  rWord = words[rSelect]
  while rQues in rQuesUsed or rWord in rWordUsed:
    continue
  if rQues not in rQuesUsed and rWord not in rWordUsed:
    rQuesUsed.append(rQues)
    rWordUsed.append(rWord)
    return rQues, rWord
  print(rQues)
  print(rWord)

def puzzleDisplay():
  grid = str.format("""
     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
     _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _ 
 0 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 1 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 2 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 3 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 4 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 5 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 6 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 7 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 8 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
 9 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
10 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
11 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
12 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
13 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
14 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
15 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
16 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
17 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
18 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
   
19 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
""","C","P","R","Q","T","U","I","Q","Y","L","U","E","O","Q","A","J","I","B","U","L",
"D","W","R","U","Y","M","W","Y","R","L","T","C","F","Y","I","N","C","H","A","L",
"V","I","P","I","P","J","K","O","N","A","E","U","N","I","T","N","O","C","X","P",
"Y","N","Z","O","N","A","F","M","N","E","H","Q","Z","M","N","K","I","Q","B","N",
"I","N","R","Z","C","T","N","E","G","L","Z","X","X","D","L","G","N","J","Z","L",
"Y","T","C","W","L","A","T","Q","H","P","O","Z","I","T","O","T","Z","T","M","V",
"C","U","P","E","J","A","I","D","C","U","F","E","U","L","E","D","V","M","C","P",
"F","V","O","L","C","Z","X","Y","A","T","H","F","S","G","O","A","S","W","T","K",
"X","Y","A","N","A","R","R","A","Y","O","C","W","E","N","A","F","O","H","Q","Z",
"Y","L","O","R","I","W","G","S","P","R","O","G","R","A","M","M","Z","M","M","C",
"F","C","A","Z","I","M","B","E","T","F","N","E","X","E","C","U","T","I","O","N",
"U","N","J","N","L","A","R","N","Q","R","E","W","Z","L","L","F","Q","H","D","W",
"N","F","S","T","I","A","B","R","Q","H","I","W","D","O","T","C","S","P","U","D",
"C","L","Q","A","T","M","M","L","A","M","Z","N","G","O","S","A","A","A","L","J",
"T","S","E","O","D","G","R","G","E","W","G","S","G","B","H","T","O","C","E","M",
"I","J","R","Z","E","J","R","E","T","A","M","R","O","F","E","J","F","L","T","E",
"O","D","G","X","D","L","J","Y","T","F","X","C","L","S","L","M","G","K","F","V",
"N","K","U","G","H","K","A","I","C","G","B","N","P","P","L","Q","E","X","Y","V",
"E","M","W","M","I","V","N","O","C","S","O","W","L","J","X","Y","W","F","H","K",
"Z","O","M","H","A","T","J","T","T","L","Q","A","S","G","I","T","L","O","D","G")
  print(grid)

def getWord(puzzle):
  coordinates = []
  while True:
     coordinateInput = input("Please enter the X and Y coordinates for the letter you want to select\
                              Remember to seperate value with a single comma: \")
  

puzzleDisplay()


