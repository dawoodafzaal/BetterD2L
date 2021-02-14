#variables
counter = 0

#question number 1
def question_one():
  ans_1 = str(input("How are you feeling today? \n A. Good \n B. Okay \n C. Bad"))
  #checking for a valid input
  if ans_1 != "A" or ans_1 != "B" or ans_1 != "C":
    print("Sorry, that is an invalid answer, please try again.")
  #if answer
  elif ans_1 == "A":
    print("That's awesome! Keep yourself occupied with tasks/hobbies which ensue joy")
  elif ans_1 == "B":
    print("Personal reccomendations I can make to better your mood is to: focus on tasks/hobbies which promote happiness, meditate, exercise and/or sleeping")
  else:
    counter = counter + 1

#asking the next question
def question_two():
  ans_2 = str(input("How much time have you spent today exercising? \n A. 60+ Minutes \n B. 20-30 Minutes \n C. 0-10"))
  #checking valid input
  if ans_2 != "A" or ans_2 != "B" or ans_2 != "C":
    print("Sorry, that is an invalid answer, please try again.")
    question_two()
  #checking which answer the user input
  elif (ans_2 == "A"):
    print("Congratulations! You are currently meeting WHO Health Guidelines, strive to maintain or increase your current level of physical activity!")
  elif (ans_2 == "B"):
    print("While you are doing some physical activity, physical health guidelines reccomend an average of sixty minutes of moderate to vigorous physical activity per day")
  else:
    print("Unfortunately you do not meet current physical health guidelines, please try incorporating more physical activity into your routine.")
    #add one to counter 
  counter = counter + 1

def question_three():
  ans_3 = str(input("When was the last time you drank water? \n A. About an hour ago \n B. A few hours ago \n C. I can not remember"))
  #checking input
  if ans_3 != "A" or ans_3 != "B" or ans_3 != "C":
    print("Sorry, that is an invalid answer, please try again.")
    question_three()
  elif (ans_3 == "A"):
    print("Great! Be sure to stay hydrated throughout the day")
  elif (ans_3 == "B" or ans_3 == "C"):
    print("Please go drink water now, staying hydrated is important to maintaining a healthy lifestyle")
    counter = counter + 1

def question_four():
  ans_4 = str(input("Am I tired \n A. Yes \n B. Kind of \n C. No"))
  if ans_4 != "A" or ans_4 != "B" or ans_4 != "C":
    print("Sorry that is an invalid answer, please try again")
    question_four()
  elif ans_4 == "A":
    print("Please take a short nap, sleep is an essential component to improve mental/physical health")
    counter = counter + 1
  elif ans_4 == "B":
    print("Maybe take a short break to relax")
  else:
    print("Great! Keep in mind that on average, most people require about 8-11 hours of sleep per day")

def check_score():
  if counter > 2:
    print("Your score is within the red zone, please take some time to focus on your mental health")

def main():
  question_one()
  question_two()
  question_three()
  question_four()

  check_score()
