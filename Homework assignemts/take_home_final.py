question 1:

question 2:


def Avengers(number):
  total = 0
  checkagain = 0
  check = []
  for N in number:
    check.append(N)
    total += N
    print(check)
    print (total)
  
  checkagain = check.pop()
  print(checkagain)
  
  if checkagain >= total - checkagain:
    return ("yes")
  else:
    return ("No, Vasya will not have enough money to give change to 100 dollars")
  


question 3:
  class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[%d,%d]" % (self.x, self.y) 

class Shape(object):
    def __init(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def area(self):
        return self.p1 * self.p2

class Square(object):
    def __init(self,x):
      self.x = x
    def area(self):
      return self.x ** 2
    def perimeter(self):
      return self.x * 4
      

class Rectangle(object):
  def __init(self, p1, p2): 
    self.p1 = p1
    self.p2 = p2
  def area(self, p1, p2):
    return self.p1 * self.p2
  def perameter(self, p1, p2):
      return (self.p1 +self.p2) * 2

class Cube(object):
  def __init(self,x):
    self.p1 = x
  def surfaceArea(self):
    return (self.p1 **2) * 6
  def volume(self):
    self.p1 ** 3
    
question 4:
"""
this code checks in chronological order of how many characters are repeated if they repeat at all.
some of this code can be found here:
http://stackoverflow.com/questions/39252731/counting-duplicate-characters
"""
def duplicate_count(text):
    num = 0
    count = {}      #this is a dictionary used to hold the character and the amount
                     # of times that character repeats.
    
    for char in text:
        
        if char in count.keys():
            count[char] += 1 #this is to keep track of which character is repeating
        else:
            count [char] = 1 #if it finds a character that is not there it appends that character
    for key in count:
        if count[key] == 1:
           num = 0
        else:
           num = count[key] - 1
    for char in count:
        if count[char] > 1
          

sample = 'abcde'
print (duplicate_count(sample))

question 5:

def Chronological(number):
  num = 0
  check = []
  for N in number:
    check.append(N)
  for num in check:
    if check[num] != check [num-1] + 1:
      return ("the number missing is" num + 1)
    else:
      return ("it is chronologically correct")


question 6

question 7
