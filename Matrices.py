import numpy as np

#------פעולות על מטריצות סימטריות-------

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# x = a + b
# print("\n print all:\n",x)
# x=x+2
# print("\n print all:\n",x)
# x=x/2
# print("\n print all:\n",x)
# x=a*b
# print("\n print all:\n",x)

#------כפל מטריצות לא סימטריות----

# c = np.array([[1, 2, 1], [0, 1, 0]])
# d = np.array([[2, 5], [6, 7], [1, 8]])
# #x2=c*d ValueError: operands could not be broadcast together with shapes (2,3) (3,2)
# x2 = c.dot(d)
# print("\nprint c:\n",c)
# print("\nprint d:\n",d)
# print("\nprint x2:\n",x2)

#----------שחלוף (transpose )מטריצות--------

# x2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
# a = x2.transpose()
# b = x2.T
# print("\n print x2:\n",x2)
# print("\n print a:\n",a)
# print("\n print b:\n",b)


