print("in total sunt 51 de exemple")
exemplu=int(input("exemplul:"))
if exemplu==1:
    from datetime import datetime
    import math
    now=datetime.now()
    print(now,'\n',now.hour,'\n',now.minute,'\n',now.day,'\n',now.month,'\n',now.year)
#############################################################################################
elif exemplu==2:
  def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer=str(input('answer:'))
    if answer == "left" or answer == "l":
      print ("This is the Verbal Abuse Room, you heap of parrot droppings!\n")
    elif answer == "right" or answer == "r":
      print ("Of course this is the Argument Room, I've told you that already!","\n")
    else:
      print ("You didn't pick left or right! Try again.\n")
  clinic()
#############################################################################################
elif exemplu==3:
  def greater_less_equal_5(answer):
    if answer>5:
      return 1
    elif answer<5:          
      return -1
    else:
      return 0
  print (greater_less_equal_5(4))
  print (greater_less_equal_5(5))
  print (greater_less_equal_5(6))
###############################################################################################
elif exemplu==4:
  def grade_converter(grade):
    if grade>=90:
        return "A"
    elif grade>=80 and grade<89:
        return "B"
    elif grade>=70 and grade<79:
        return "C"
    elif grade>=65 and grade<69:
        return "D"
    else:
        return "F"
  print (grade_converter(92))
  print (grade_converter(70))
  print (grade_converter(61))
#######################################################################################
elif exemplu==5:
  x=""
  print(x.isalpha()) #isalpha() = mereu false
  def tax(bill):
    bill *= 1.08
    print ("With tax: %f" % bill)
    return bill
  def tip(bill):
    bill *= 1.15
    print ("With tip: %f" % bill)
    return bill
  meal_cost = 100
  meal_with_tax = tax(meal_cost)
  meal_with_tip = tip(meal_with_tax)
#################################################################################
elif exemplu==6:
  def square(n):
    squared = n ** 2
    print ("%d squared is %d." % (n, squared))
    return squared
  square(int(input()))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
elif exemplu==7:
  def power(base,exponent):  # Add your parameters here!
    result = base ** exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))
  power(int(input()),int(input()))  # Add your arguments here!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
elif exemplu==8:
  print("from math import (_____)")
#####################################################################################
elif exemplu==9:
  import math # Imports the math module
  everything = dir(math) # Sets everything to a list of things from math
  print (everything,"\n") # Prints 'em all!
####################################################################################
elif exemplu==10:
  def func(a, b, c=2): 
    return a + b + c
  print(func(int(input()), int(input()))) 
######################################################################################
elif exemplu==11:
  def shut_down(s):
    if s == "yes":
      return "Shutting down"
    elif s == "no":
      return "Shutdown aborted"
    else:
      return "Sorry"
  print (shut_down(str(input())))
###################################################################################
elif exemplu==12:
  def distance_from_zero(a):
    if type(a)==int or type(a)==float:
      return abs(a)
    else:
      return "Nope"
  print(distance_from_zero(int(input())))
###################################################################################
elif exemplu==13:
  def hotel_cost(nights):
    return 140 * nights
  def plane_ride_cost(city):
    if city == "Charlotte":
      return 183
    elif city == "Tampa":
      return 220
    elif city == "Pittsburgh":
      return 222
    elif city == "Los Angeles":
      return 475
  def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
      cost -= 50
    elif days >= 3:
      cost -= 20
    return cost
  def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
  print (trip_cost("Los Angeles",5,600))
##########################################################################################################
elif exemplu==14:
  residents = {'Puffin' : 1020, 'Sloth' : 105, 'Burmese Python' : 106}
  print (residents['Puffin']) 
  print (residents['Sloth'])
  print (residents['Burmese Python'])
####################################################################################
elif exemplu==15:
  menu = {} # Empty dictionary
  menu['Chicken Alfredo'] = 14.50 
  print (menu['Chicken Alfredo'])
  menu['Hamburger'] = 8.50
  menu['Pizza Slice'] = 3.50
  menu['Salad'] = 10.00
  print ("There are " + str(len(menu)) + " items on the menu.")
  print (menu)
#################################################################################
elif exemplu==16:
  # key - animal_name : value - location 
  zoo_animals = { 'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'}
  del (zoo_animals['Unicorn'])
  del (zoo_animals['Sloth'])
  del (zoo_animals['Bengal Tiger'])
  zoo_animals['Rockhopper Penguin'] = 'Plains Exhibit'
  print (zoo_animals)
########################################################################################
elif exemplu==17:
  backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
  backpack.remove('dagger')
  print(backpack)
#################################################################################
elif exemplu==18:
  inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
  }
  inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
  inventory['pouch'].sort()
  print(inventory['pouch'])
  inventory['pocket'] = ['seashell', 'strange berry', 'lint']
  inventory['backpack'].sort()
  inventory['backpack'].remove('dagger')
  print (inventory['backpack'])
  inventory['gold'] = inventory['gold'] + 50
  print(inventory['gold'])
  print(inventory)
#######################################################################################
elif exemplu==19:
  prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
  stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
  for x in prices:
    if x == 'apple':
      print (x)
      print ("price: %s" % prices[x])
      print ("stock: %s" % stock[x])
  total = 0
  for food in prices:
    print (prices[food] * stock[food])
    total = total + prices[food] * stock[food]
  print (total)
###########################################################################################
elif exemplu==20:
  shopping_list = ["banana", "orange", "apple"]
  stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
  prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
  def compute_bill(food):
    total = 0
    for item in food:
      total = total + prices[item]
      return total
      print(total)
  def comput_bill(foo):
    total = 0
    for item in foo:
      if stock[item] > 0:
        total += prices[item]
        stock[item] -= 1
        return total
        print(total)
######################################################################################################
elif exemplu==21:
  lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
  }
  alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
  }
  tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
  }
  students = [lloyd, alice, tyler]
  for student in students:
    print (student["name"])
    print (student["homework"])
    print (student["quizzes"])
    print (student["tests"])
  def average(numbers):
    total = float(sum(numbers))
    return total/len(numbers)
  def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    total = homework *.1 + quizzes * .3 + tests * .6
    return total
  def get_letter_grade(score):
    if score >= 90:
      return "A"
    elif score >=80:
      return "B"
    elif score >=70:
      return "C"
    elif score >=60:
      return "D"
    else:
      return "F"
  print (get_letter_grade(get_average(lloyd)))
  def get_class_average(class_list):
    results = []
    for student in class_list:
      student_avg = get_average(student)
      results.append(student_avg)
    return average(results)
  students = [alice, lloyd, tyler]
  score=(get_average(lloyd)+get_average(alice)+get_average(tyler))/3
  print (score)
  def get_letter_grade(score):
    if score >= 90:
      return "A"
    elif score >=80:
      return "B"
    elif score >=70:
      return "C"
    elif score >=60:
      return "D"
    else:
      return "F"
  print (get_letter_grade(score))
#####################################################################################
elif exemplu==22:
  x=int(input())
  for i in range(0, x):
    print (i)
###############################################################################
elif exemplu==23:
  m = [1, 2, 3]
  n = [4, 5, 6]
  def join_lists(x, y):
	  return x + y
  print (join_lists(m, n))
#################################################################################
elif exemplu==24:
  n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
  def flatten(lists):
    results = []
    for numbers in lists:
      for number in numbers:
        results.append(number)
    return results
  print (flatten(n))
#####################################################################################
elif exemplu==25:
  #       JOACĂ
  from random import randint
  board = []
  for i in range(5):
    board.append(['O'] * 5)
  def print_board(board_in):
    for row in board:
      print (row)
    for row in board:
      print (" ".join(row))
  print_board(board)
  def random_row(board_in):
    return randint(0, len(board_in)-1)
  def random_col(board_in):
    return randint(0, len(board_in)-1)
  random_row(board)
  random_col(board)
  ship_row = random_row(board)
  ship_col = random_col(board)
  print (ship_row)
  print (ship_col)
  for turn in range(4):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    if guess_row == ship_row and guess_col == ship_col:
      print ("Congratulations! You sank my battleship!")   
      break
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print ("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
      print_board(board)
      if (turn == 3):
        print ("Game Over")
      print_board(board)
####################################################################################
elif exemplu==26:
  choice = str(input('Enjoying the course? (y/n)'))
  while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = str(input("Sorry, I didn't catch that. Enter again: "))
#########################################################################################################
elif exemplu==27:
  import random
  print ("Lucky Numbers! 3 numbers will be generated.")
  print ("If one of them is a '5', you lose!")
  count = 0
  while count < 3:
    num = random.randint(1, 6)
    print( num)
    if num == 5:
      print ("Sorry, you lose!")
      break
    count += 1
  else:
    print ("You win!")
######################################################################################################
elif exemplu==28:
  from random import randint
  random_number = randint(1, 10)
  guesses_left = 3
  while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
      print ("You win!")
      break
    guesses_left -= 1
  else:
    print ("You lose.")
############################################################################################################
elif exemplu==29:
  thing = "spam!"
  for c in thing:
    print (c)
  word = "eggs!"
  for c in word:
    print (c)
######################################################################################
elif exemplu==30:
  list_a = [3, 9, 17, 15, 19]
  list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
  for a, b in zip(list_a, list_b):
    print (max(a, b))
#################################################################################################
elif exemplu==31:
  def digit_sum(n):
    total = 0
    string_n = str(n)
    for char in string_n:
      total += int(char)
    return total
  #Alternate Solution:
  #def digit_sum(n):
  #  total = 0
  #  while n > 0:
  #    total += n % 10
  #    n = n // 10
  #  return total
  print (digit_sum(1234))
############################################################################################
elif exemplu==32:
  def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  print (factorial(4))
###################################################################################################################
elif exemplu==33:
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
  def scrabble_score(word):
    word = word.lower()
    total = 0
    for letter in word:
      for leter in score:
        if letter == leter:
          total = total + score[leter]
    return total
  print (scrabble_score(str(input())))
###########################################################################################################################
elif exemplu==34:
  def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)
    return result
  print (censor("this hack is wack hack", "hack"))
  def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count
  print (count([1, 2, 1, 1], 1))
###########################################################################################################################
elif exemplu==35:
  def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    inputlist = sorted(inputlist)
    outputlist = [inputlist[0]]
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
    return outputlist
  print (remove_duplicates([1, 1, 2, 2,3,3]))
###########################################################################################################################
elif exemplu==36:
  def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        index_1 = len(sorted_list)//2 - 1
        index_2 = len(sorted_list)//2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
  print (median([2, 4, 5, 9,]))
###########################################################################################################################
elif exemplu==37:
  grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
  def grades_sum(scores):
    total = 0
    for score in scores: 
      total += score
    return total
  print (grades_sum(grades))
 
  def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average
  print (grades_average(grades))
  
  def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
      variance += (average - score) ** 2
    return variance / len(scores)
  print (grades_variance(grades),"\n")
  
  for grade in grades:
    print(grade)
    print(grades_sum(grades))
    print(grades_average(grades))
    print("----------------------")
###########################################################################################################################
elif exemplu==38:
  evens_to_50 = [i for i in range(51) if i % 2 == 0]
  print (evens_to_50)
  doubles_by_3 = [x*2 for x in range(1, 6) if (x * 2) % 3 == 0]
  print (doubles_by_3)
  even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]
  print (even_squares)
  cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
  print (cubes_by_four)
###########################################################################################################################
elif exemplu==39:
  my_list = range(16)
  print (filter(lambda x: x % 3 == 0, my_list))
  languages = ["HTML", "JavaScript", "Python", "Ruby"]
  print (filter(lambda x: x == "Python", languages))
  squares = [x**2 for x in range(1,11)]
  print (filter(lambda x: x>30 and x<70, squares))
###########################################################################################################################
elif exemplu==40:
  garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
  message = garbled[::-2]
  print (message)
  garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
  message = filter(lambda x: x!='X',garbled)
  print (message)
###########################################################################################################################
elif exemplu==41:
  print (5 >> 4)  # Right Shift
  print (5 << 1)  # Left Shift
  print (8 & 5)   # Bitwise AND
  print (9 | 4)   # Bitwise OR
  print (12 ^ 42) # Bitwise XOR
  print (~88)     # Bitwise NOT
  print (0b1)    #1 virgula=intr-un rand
  print (0b10)   #2
  print (0b11)   #3
  print (0b100)  #4
  print (0b101)  #5
  print (0b110)  #6
  print (0b111)  #7
  print ("******")
  print (0b1 + 0b11)
  print (0b11 * 0b11)
###########################################################################################################################
elif exemplu==42:
  print (bin(1)) #codul binar
  print (bin(2))
  print (bin(3))
  print (bin(4))
  print (bin(5))
###########################################################################################################################
elif exemplu==43:
  print (int("1",2))
  print (int("10",2))
  print (int("111",3))
  print (int("0b100",2))
  print (int(bin(5),2))
  print (int("11001001", 3))
###########################################################################################################################
elif exemplu==44:
  shift_right = 0b1100
  shift_left = 0b1
  shift_right = shift_right >> 2
  shift_left = shift_left << 2
  print (bin(shift_right))
  print (bin(shift_left))
###########################################################################################################################
elif exemplu==45:
  print (bin(0b1110 & 0b101)) #0b+(101, ultima cifra, and 1110, ultima cifra, numarul de cifre comune)
  print (bin(0b1110 | 0b101)) #0b+(101, ultima cifra, or 1110, ultima cifra, cel mai mare nr de cifre)
  print (bin(0b1111 ^ 0b0111))  #0b+(inversarea numerelor, ??)
  print (~123) # -(123+1)
###########################################################################################################################
elif exemplu==46:
  def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
      return "on"
    else:
      return "off"
###########################################################################################################################
elif exemplu==47:
  def flip_bit(number, n):
    bit_to_flip = 0b1 << (n -1)
    result = number ^ bit_to_flip
    return bin(result)
  print (flip_bit(21, 4))
###########################################################################################################################
elif exemplu==48:
  class Animal(object):
    def __init__(self, name):
      self.name = name
  zebra = Animal("Jeffrey")
  print (zebra.name)
###########################################################################################################################
elif exemplu==49:
  class Animal(object):
    def __init__(self, name, age, is_hungry):
      self.name = name
      self.age = age
      self.is_hungry = is_hungry
  zebra = Animal("Jeffrey", 2, True)
  giraffe = Animal("Bruce", 1, False)
  panda = Animal("Chad", 7, True)
  print (zebra.name, zebra.age, zebra.is_hungry)
  print (giraffe.name, giraffe.age, giraffe.is_hungry)
  print (panda.name, panda.age, panda.is_hungry)
###########################################################################################################################
elif exemplu==50:
  class ShoppingCart(object):
    def __init__(self, customer_name):
      self.customer_name = customer_name
      self.items_in_cart = {}
    def add_item(self, product, price):
      """Add product to the cart."""
      if not product in self.items_in_cart:
        self.items_in_cart[product] = price
        print (product + " added.")
      else:
        print (product + " is already in the cart.")
    def remove_item(self, product):
      """Remove product from the cart."""
      if product in self.items_in_cart:
        del self.items_in_cart[product]
        print (product + " removed.")
      else:
        print (product + " is not in the cart.")
  my_cart = ShoppingCart("Eric")
  my_cart.add_item("Ukelele", 10)
###########################################################################################################################
elif exemplu==51:
  class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
      self.angle1 = angle1
      self.angle2 = angle2
      self.angle3 = angle3
    def check_angles(self):
      if (self.angle1 + self.angle2 + self.angle3) == 180:
        return True
      else:
        return False
  class Equilateral(Triangle):
    angle = 60
    def __init__(self):
      self.angle1 = self.angle
      self.angle2 = self.angle
      self.angle3 = self.angle
  my_triangle = Triangle(30, 60, 90)
  print (my_triangle.number_of_sides)
  print (my_triangle.check_angles())
