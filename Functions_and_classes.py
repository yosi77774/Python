

#--------הגדרת פעולה בשפת python מתבצעת על ידי ההוראה def נדגים זאת:------

# def SignCheck(x):
#  if x > 0:
#   print(x,"is positive")
#  elif x < 0:
#   print(x,"is negative")
#  else:
#   print(x,"is zero")
# SignCheck(-10)
# for i in [-2,0,10,-10,0,3]:
#  SignCheck(i)

#------נדגים את אותה פעולה אך הפעם הפעולה תחזיר ערך תוך שימוש במשפט return------

# def SignCheck(x):
#  if x > 0:
#   return "positive"
#  elif x < 0:
#   return "negative"
#  else:
#   return "zero"
# for i in [-2,0,10,-10,0,3]:
#  print(i, "is", SignCheck(i))

#------פעולות ב- python יכולות להחזיר יותר מערך אחד. נדגים זאת:-----

# def NewDiv(x,y):
#  a=x//y
#  b=x%y
#  return a , b
# n1,n2 = NewDiv(14,4)
# print(n1,n2)
# for x in [[4, 2],[7,3]]:
#  print(NewDiv(x[0],x[1]))

#-------מחלקות-----
#נדגים מחלקה בסיסית המייצגת נקודה המורכבת מ-2 ערכים (x ו- y)

# class MyPoint(object):
#  def __init__(self, x,y):
#   self.x = x
#   self.y = y
#  def addX(self, x):
#   self.x += x
#  def addY(self, y):
#   self.y += y
#
# p=MyPoint(0,0)
# p.x=100
# p.y=100
# p.addX(-10)
#
# p.addY(10)
# print("obj p: x=",p.x,"y=",p.y)
# Points_list = []
# for i in range(10):
#  p=MyPoint(i,i)
#  p.addX(-10)
#  p.addY(10)
#  p.x=100
#  Points_list.append(p)
# for obj in Points_list:
#  print("x=",obj.x,"y=",obj.y)

# ניתן להגדיר בפעולה הבונה פרמטרים אופציונאליים, בדוגמה הבאה הגדרנו את הערך 0 כברירת מחדל עבור
# x ו- y .באופן זה ניתן ליצור מנגנון הדומה לפעולות בונות מרובות. נדגים זאת:

# class MyPoint(object):
#  def __init__(self, x=0,y=0):
#   self.x = x
#   self.y = y
#  def addX(self, x):
#   self.x += x
#  def addY(self, y):
#   self.y += y
#
# p1=MyPoint(5,5)
#
# p1.x=100
# p1.y=100
# p1.addX(-10)
# p1.addY(10)
# print("obj p1: x=",p1.x,"y=",p1.y)
# p2=MyPoint()
# p2.addX(-10)
# p2.addY(10)
# print("obj p2: x=",p2.x,"y=",p2.y)
# Points_list = []
# for i in range(10):
#  p=MyPoint(i,i)
#  p.addX(-10)
#  p.addY(10)
#  p.x=100
#  Points_list.append(p)
# for obj in Points_list:
#  print("x=",obj.x,"y=",obj.y)

# נשפר את המחלקה point כך שיקבעו ערכים אקראיים עבור x ו- y .כמו כן נעצב את פלט לנתוני המחלקה.
# import numpy as np
# class point(object):
#  def __init__(self):
#   self.x = np.random.uniform(-1,1)
#   self.y = np.random.uniform(-1,1)
#   if self.x > self.y:
#    self.label = 1
#   else:
#    self.label = -1
#  def __repr__(self):
#    return "x="+str(self.x)+" y="+str(self.y)+" label="+str(self.label)+"\n"
# p= point()
# print(p)
# Points_list = []
# for i in range(10):
#  Points_list.append(point())
# print(Points_list)