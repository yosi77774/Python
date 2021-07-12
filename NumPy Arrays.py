import numpy as np

#-------משימה 2 :מערך חד מימדי--------
# x = np.array([2, 4, 6, 8, 10])
# print(type(x))
# print(x.shape)
# print(x[0], x[1], x[4])
# x[0] = 5
# print(x)

#--------משימה 3 :הגדרת מערך דו מימדי-------
#
# x2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
# print("\nprint all:\n",x2)
# print("\ntype: ", type(x2))
# print("\nshape: ", x2.shape)
# print("\ndata from row0: ",x2[0,0], x2[0,1], x2[0,4])
# print("\ndata from row1: ",x2[1,0], x2[1,1], x2[1,4])
# print("\nall row0: ",x2[0])
# print("\nall row1: ",x2[1])
# x2[0,0] = 500
# x2[1,4] = 100
# print("\nall new array:\n",x2)

#---------משימה 4 :מערך שלוש מימדים---------

# x3 = np.array([ [ [1, 2, 3, 4],
#                   [5, 6, 7, 8]
#                 ],
#                 [
#                   [10, 20, 30, 40],
#                   [50, 60, 70, 80]
#                 ]
#              ])
# print("\nprint all:\n",x3)
# print("\ntype: ", type(x3))
# print("\nshape: ", x3.shape)
# print("\n[0,0,0]: ",x3[0,0,0])
# print("\n[1,1,3]: ",x3[1,1,3])
# print("\nall row 0,0: ",x3[0,0])
# print("\nall row 0,1: ",x3[0,1])
# print("\nall row 1,0: ",x3[1,0])
# print("\nall row 1,1: ",x3[1,1])
# x3[0,0,0] = 500
# x3[1,1,3]=100
# print("\nprint all:\n",x3)

#-----משימה 5 :אתחול מערך ללא צורך בהכנסת ערכים מראש---------

# a = np.zeros((4,4))
# print("\n print all:\n",a)
# b = np.ones((1,8))
# print("\n print all:\n",b)
# c = np.full((2,2), 7)
# print("\n print all:\n",c)
# d = np.eye(5,5)
# print("\n print all:\n",d)
# e = np.random.uniform(size=[3,5])
# print("\n print all:\n",e)
# f = np.random.uniform(-1,1,size=[2,4])
# print("\n print all:\n",f)

#-----דרכים נוספת לבניית מערך מספרים אקראיים בין 0 ל-1:-------------

# g = np.random.random_sample((5,))
# print("\n print all:\n",g)
# h = np.random.random_sample((5,5))
# print("\n print all:\n",h)

#---------משימה 6 :חיתוך מערכים חד מימדיים----------

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print("\nprint all:\n",x)
# print("start=1:stop=7:step=no ",x[1:7])
# print("start=5:stop=no:step=no ",x[5:])
# print("start=no:stop=5:step=no ",x[:5])
# print("start=1:stop=7:step=2 ",x[1:7:2])
# print("start=no:stop=no:step=-1 ",x[::-1])
# print("start=-3:stop=-6:step=-1 ",x[-3:-6:-1])


#--------משימה 7 :חיתוך מערכים דו מימדיים----------

# x2 = np.array([ [1,2,3,4,5],
# [6,7,8,9,10],
# [11,12,13,14,15],
# [16,17,18,19,20],
# [21,22,23,24,25] ])
# print("\nprint all:\n",x2)
# print("FROM:start=1:stop=4:step=no TO:start=1:stop=4:step=no\n",x2[1:4,1:4])
# print("FROM:start=2:stop=no:step=no TO:start=2:stop=no:step=no\n",x2[2:,2:])
# print("FROM:start=no:stop=no:step=2 TO:start=no:stop=no:step=2\n",x2[::2,::2])
# print("FROM:start=no:stop=no:step=-1 TO:start=no:stop=no:step=-1\n",x2[::-1,::-1])
# print("FROM:start=-2:stop=no:step=-1 TO:start=-2:stop=no:step=-1\n",x2[-2::-1,-2::-1])

#---------משימה 8 :עיצוב/שינוי מחדש של מבנה מערך חד מימדי-----------

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print("\n print all:\n",x)
# a = np.reshape(x,(5, 2))
# print("\n print all:\n",a)
# b = np.reshape(x,(10, 1))
# print("\n print all:\n",b)
# c = np.reshape(x,(2, 5))
# print("\n print all:\n",c)

#-------משימה 9 :עיצוב/שינוי מחדש של מבנה מערך דו מימדי-----------

# x2 = np.array([[1,2,3,4], [5,6,7,8]])
# d = np.reshape(x2,8)
# print("\n print all:\n",d)
# e = np.reshape(x2,(8,1))
# print("\n print all:\n",e)
# #print(x2.shape,x2.shape[0],x2.shape[1])
# f = np.reshape(x2,(x2.shape[0]*x2.shape[1], 1))
# print("\n print all:\n",f)

#---------משימה 10 :פיצול מערכים על ידי הפעולה split

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# x_split = np.split(x,2)
# print("\nprint all:\n",x)
# print("\nprint all split:\n",x_split)
# print("\nprint array[0]:\n",x_split[0])
# print("\nprint array[1]:\n",x_split[1])

#פיצול מערך באופן לא סימטרי נעשה עם split_array

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# x_split = np.array_split(x,3)
# print("\nprint all:\n",x)
# print("\nprint all split:\n",x_split)
# print("\nprint array[0]:\n",x_split[0])
# print("\nprint array[1]:\n",x_split[1])
# print("\nprint array[2]:\n",x_split[2])

#----משימה 11 :חיבור מערכים על ידי הפעולות vstack ו- hstack---------

# x1 = np.array([1, 2, 3, 4, 5 ])
# x2 = np.array([6, 7, 8, 9, 10])
# x = np.vstack((x1,x2))
# print("\nprint all:\n",x)
# y = np.hstack((x1,x2))
# print("\nprint all:\n",y)

#---------משימה 12 :פעולות אריתמטיות ולוגיות על מערכים-------

# x1 = np.array([1, 2, 3, 4, 5 ])
# x2 = np.array([1, 3, 3, 6, 7 ])
# x3 = x1 + x2
# x4 = x1 / x2
# x5 = x1 * x2
# x6 = x1 - x2
# print("\n x1 + x2: \n",x3)
# print("\n x1 / x2: \n",x4)
# print("\n x1 * x2: \n",x5)
# print("\n x1 - x2: \n",x6)

#ניתן כמובן לבצע גם פעולות לוגיות כמודגם בקוד הבא:

# x1 = np.array([1, 2, 3, 4, 5 ])
# x2 = np.array([1, 3, 3, 6, 7 ])
# x3 = x1 == x2
# x4 = x1 < x2
# x5 = x1 > x2
# x6 = x1 != x2
# print("\n x1 == x2: \n",x3)
# print("\n x1 > x2: \n",x4)
# print("\n x1 < x2: \n",x5)
# print("\n x1 != x2: \n",x6)




