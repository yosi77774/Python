import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# #-----------משימה 1 :יצירת קו ישר על גבי מערכת צירים--------------
# # הפעולה plot קובעת מהם הנתונים שיש להציג על הגרף.
# plt.plot([1, 2, 3, 4])
# # הפעולה title קובעת את הכותרת של הגרף.
# plt.title('My Line')
# # הפעולה axis קובעת את טווח הערכים של מערכות הצירים לפי הפירוט הבא: [ymax, ymin, xmax, xmin]
# plt.axis([0, 3, 0, 5])
# # הפעולה xlabel ו- ylabel קובעים את הכותרות לצירים X ו- Y בהתאמה.
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
#
# # ------------------------------
#
# # הגרסה המינימלית ליצירת קו.
# plt.plot([1, 4])
# plt.show()


#--------משימה 2 :פיזור נקודות על גבי מערכות צירים-----------

# *הכיתוב go מציין שמדובר על נקודות בצורת עיגול 'o 'בצבע ירוק 'g'
# plt.plot([1, 2, 3, 4, 5], [2, 4, 8, 16, 32], 'go')
# plt.axis([0, 6, 0, 35])
# plt.title('My dots')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# כמובן ניתן לשרטט מספר מערכות צירים בצבעים שונים להלן דוגמה:

# הפעולה arange.np מייצרת סדרה של מספרים מהערך הראשון שהפעולה מקבלת עד לערך האחרון
# בקפיצות של הערך השלישי שהפעולה מקבלת.
# t = np.arange(0.0, 10.0, 0.5)
# print(t)
# plt.plot(t, t, 'r--')
# plt.plot(t, t**2, 'g^')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

#----------משימה 3 :שרטוט אות סינוס------------

# t = np.arange(0.0, 2.0, 0.01)
# s = 3*np.sin(2 * np.pi * t)
# plt.plot(t, s)
# plt.title("Sine wave")
# plt.xlabel("time (s)")
# plt.ylabel("voltage (V)")
# plt.show()

#ניתן לשפר את מראה האות על ידי הוספת רשת קווים פנימית (grid (כמו כן קביעת הערכים של מערכת
# הצירים. נדגים זאת:

# t = np.arange(0.0, 2.0, 0.01)
# s = 3*np.sin(2 * np.pi * t)
# plt.plot(t, s)
# plt.axis([0, 2, -3.5, +3.5])
# plt.grid()
# plt.title("Sine wave")
# plt.xlabel("time (s)")
# plt.ylabel("voltage (V)")
# plt.show()

#---------משימה 4 :עיצוב מערכת הצירים-------

# ax = plt.gca()
# ax.spines['left'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['bottom'].set_position('zero')
# ax.spines['top'].set_color('none')
# plt.xlim([-10, 10])
# plt.ylim([-10, 10])
# plt.grid()
# plt.show()

#---------משימה 5 :שרטוט מספר גרפים על גבי מערכת צירים אחת----------

# ax = plt.gca()
# ax.spines['left'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['bottom'].set_position('zero')
# ax.spines['top'].set_color('none')
# plt.xlim([-10, 10])
# plt.ylim([-10, 10])
# plt.grid()
# x = np.arange(-10,10,0.1) #x = np.linspace(-10,10,10)
# y1 = 0.5*x+2.5
# y2 = x+2.5
# y3 = 2*x+2.5
# plt.plot(x, y1, '-r', label='y=0.5x+2.5')
# plt.plot(x, y2, '-g', label='y=x+2.5')
# plt.plot(x, y3, '-b', label='y=2x+2.5')
# plt.legend(loc='upper left')
# plt.show()

#----------משימה 6 :פיזור נקודות בצבעים שונים על גבי מערכות צירים דו-מימד----------

# x1 = [1,2,3,4,5]
# y1 = [5,4,3,3,6]
# x2 = [6,7,8,9,10]
# y2 = [4,3,4,2,1]
# plt.scatter(x1, y1, c='red')
# plt.scatter(x2, y2, c='blue')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

#--------משימה 7 :פיזור נקודות בצבעים שונים על גבי מערכות צירים שלוש מימדים--------

# data = np.array( [ [ 6.0 , 7.0, 5.0],
# [ 2.0 , 3.0, 7.0],
# [ 3.0 , 7.0, 2.0],
# [ 4.0 , 4.0, 8.0],
# [ 5.0 , 8.0, 9.0],
# [ 6.0 , 5.0, 7.0],
# [ 7.0 , 9.0, 4.0],
# [ 8.0 , 5.0, 1.0],
# [ 8.0 , 2.0, 3.0],
# [10.0 , 2.0, 5.0] ])
# categories = np.array([0,1,1,1,1,2,2,2,2,2])
# colormap = np.array(['r', 'g', 'b'])
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(data[:,0], data[:,1],data[:,2], s=150, c=colormap[categories])
# plt.show()

#-------משימה 8 :עיצוב מערכת הצירים-----------

# ax = plt.gca()
# ax.spines['left'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['bottom'].set_position('zero')
# ax.spines['top'].set_color('none')
# plt.xlim([-4, 4])
# plt.ylim([-1, 10])
# plt.grid()
# x = np.arange(-3.0, 3.0, 0.1)
# plt.plot(x, x**2, color = "b")
# plt.show()

