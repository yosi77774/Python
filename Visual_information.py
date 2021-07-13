from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#------כדי לפתוח את התמונה תוך שימוש בספריה PIL נכתוב את הקוד הבא:------

# img = Image.open("dog.jpg")
# width, height = img.size
# print(width, height)
# img.show()

#-----משימה 2 :פעולות על תמונה-------

# img = Image.open("dog.jpg")
# width, height = img.size
#
# img45 = img.rotate(45) #הפעולה rotate.img מקבלת זווית ומחזירה תמונה הכוללת הטייה בזווית הרצויה
# area = (width/2-200, height/2-200, width/2+200, height/2+200) #הפעולה crop.img מבצעת חיתוך של קטע מתמונה על פי פרמטר שנקלט דרך המשתנה area
# img_crop = img.crop(area)
# newsize = (width//4, height//4)#הפעולה resize.img מבצעת שינוי בגודל התמונה על פי פרמטר המתקבל דרך המשנה newsize
# img_resize = img.resize(newsize)
# #הפעולה transpose.img מבצעת היפוך לתמונה על פי הפרמטר שהיא מקבלת. בדוגמה שלנו ההפוך יהיה
# #(Image.FLIP_LEFT_RIGHT) לשמאל מימין
# img_transpose = img.transpose(Image.FLIP_LEFT_RIGHT)
# img45.save("dog45.jpg")
# img_crop.save("dog_cropped.jpg")
# img_resize.save("dog_resized.jpg")
# print("Old image size:", img.size)
# print("New image size:", img_resize.size)
# img45.show()
# img_crop.show()
# img_resize.show()
# img_transpose.show()

#----------משימה 3 :המרת צבעים בתמונה--------

# img = Image.open("dog.jpg")
# img1 = img.convert("LA")
# img2 = img.convert("1")
# img1.show()
# img2.show()

#------------פירוק התמונה לצבעים המרכיבים אותה-------

# img = Image.open("dog.jpg")
# width, height = img.size
# data = img.getdata()
# R = []
# G = []
# B = []
#
# for i in data:#נגדיר 3 מערכים בשמות R G ן-B ונשמור בכל אחד מבע בודד
#  R.append((i[0], 0, 0))
#  G.append((0, i[1], 0))
#  B.append((0, 0, i[2]))
# imgR = Image.new(mode = "RGB", size = (width, height))
# imgG = Image.new(mode = "RGB", size = (width, height))
# imgB = Image.new(mode = "RGB", size = (width, height))
# imgR.putdata(R)
# imgG.putdata(G)
# imgB.putdata(B)
# imgR.show()
# imgG.show()
# imgB.show()


#---------קוד בשפת python הממיר תמונה צבעונית לתמונה בינארית-------

# img = Image.open("dog.jpg")
# width, height = img.size
# data = img.getdata()
# BIN = []
# for i in data:
#  avg = (i[0]+i[1]+i[2])/3
#  if avg<60:
#   BIN.append((255, 255, 255))
#  else:
#   BIN.append((0, 0, 0))
# imgBIN = Image.new(mode = "RGB", size = (width, height))
# imgBIN.putdata(BIN)
# imgBIN.show()

#-----ניצור תמונה בשחור לבן במקום תמונה בינארית.----


# img = Image.open("dog.jpg")
# width, height = img.size
# data = img.getdata()
# BIN = []
# for i in data:
#  avg = int((i[0]+i[1]+i[2])/3)
#  BIN.append((avg, avg, avg))
# imgBIN = Image.new(mode = "RGB", size = (width, height))
# imgBIN.putdata(BIN)
# imgBIN.show()


#------- משימה 4 :יצירת תמונה תוך שימוש בכלי numpy---------

# pixels =[
# [ [255,0,0],[255,255,255],[0,0,0],[0,255,0],[255,0,255] ],
# [ [255,255,0],[0,255,255],[0,0,255],[100,100,100],[50,50,50] ]
# ]
# array = np.array(pixels, dtype=np.uint8)
# new_image = Image.fromarray(array)
# new_image.save("MyPic.jpg")
# plt.imshow(new_image)
# plt.show()

#---------עד כה השתמשנו בפעולה show כדי להציג את התמונה. ניתן להיעזר בספריה matplotlib גם כן להציג-------

# pixels = np.zeros([400,400,3],dtype=np.uint8)
# pixels[:,:] = [0, 128, 100]
# print(pixels[:,:])
# img = Image.fromarray(pixels)
# plt.imshow(img)
# plt.show()

#-----------ניתן ליצור תמונות הכוללת יותר מצבע אחד. להלן דוגמה:------

# pixels = np.zeros([100,200,3],dtype=np.uint8)
# pixels[:,:100] = [255, 0, 0]
# pixels[:,100:] = [0, 0, 255]
# img = Image.fromarray(pixels)
# img.show()

#---------יצרת ריבוע בתוך ריבוע-----------

# pixels = np.zeros([100,200,3],dtype=np.uint8)
# pixels[:,:100] = [255, 0, 0]
# pixels[:,100:] = [0, 0, 100]
# pixels[25:75,25:75] = [0, 0, 255]
# pixels[25:75,125:175] = [255, 0, 0]
# print(pixels.shape,type(pixels))
# img = Image.fromarray(pixels)
# img.show()


# ----------משימה 5 :קריאת תמונה לתוך מערך n-------

# img = Image.open("dog.jpg")
# img.load()
# data = np.array(img, dtype=np.uint8)
# data[0:100,0:100]=[255, 0, 0]
# data[100:200,100:200]=[0, 255, 0]
# data[200:300,200:300]=[0, 0, 255]
# data[300:400,300:400]=[255, 0, 255]
# data[400:500,400:500]=[0, 255, 255]
# data[500:600,500:600]=[255, 255, 255]
# img = Image.fromarray(data)
# img.show()

#------משימה 6 :חיפש מאפיינים לזיהוי פריטים בתמונה (הכנות למשחק ים יבשה בגרסת מכונה לומדת)

# img = Image.open("Photos/sea0.jpg")
# img.load()
# sea0 = np.array(img, dtype=np.uint8)
# print ("sea0 - Green =" , sea0[:,:,1].sum() / sea0[:,:,1].size)
# print ("sea0 - blue =" , sea0[:,:,2].sum() / sea0[:,:,2].size)
# img = Image.open("Photos/land0.jpg")
# img.load()
# land0 = np.array(img, dtype=np.uint8)
# print ("land0 - Green =" , land0[:,:,1].sum() / land0[:,:,1].size)
# print ("land0 - blue =" , land0[:,:,2].sum() / land0[:,:,2].size)

#------בשלב הבא נבנה 2 רשימות הכולות את ממוצע הצבע ירוק בכל אחד מ- 20 התמונות לפי הפרדה בין תמונות------
#------ים לתמונות יבשה:-----

# sea_list = list()
# land_list = list()
#
# for i in range(5):
#  img = Image.open("Photos/sea" + str(i) + ".jpg")
#  img.load()
#  data = np.array(img, dtype=np.uint8)
#  sea_list.append(data[:,:,1].sum() / data[:,:,1].size)
#
#  img = Image.open("Photos/land" + str(i) + ".jpg")
#  img.load()
#  data = np.array(img, dtype=np.uint8)
#  land_list.append(data[:,:,1].sum() / data[:,:,1].size)
# print("\nsea_list:\n",sea_list)
# print("\nland_list:\n",land_list)


#---------בשלב הבא נבנה גרפים המציגים את הנתונים שקיבלנו מהשלב הקודם אך הפעם נציג את היחס בין ממוצע----------
# ---------------כל 2 צבעים בכל תמונה לפי חלוקה בין תמונות ים לתמונות יבשה:-----------

sea_colors = list()
for i in range(5):
 img = Image.open("Photos/sea" + str(i) + ".jpg")
 img.load()
 data = np.array(img, dtype=np.uint8)
 sea_colors.append([data[:,:,color].sum() / data[:,:,color].size for color in range(3)])#נכניס לרשימה את סה"כ שלושת הצבעים לכל תמונה
land_colors = list()
for i in range(5):
 img = Image.open("Photos/land" + str(i) + ".jpg")
 img.load()
 data = np.array(img, dtype=np.uint8)
 land_colors.append([data[:,:,color].sum() / data[:,:,color].size for color in range(3)])
sea_array = np.array(sea_colors)
land_array = np.array(land_colors)
plt.figure(1)#נייצג את התוצאות באמצעות גרפים שמוגדרים בהמשך הקוד
plt.subplot(131)
x1 = sea_array[:,0]
y1 = sea_array[:,1]
x2 = land_array[:,0]
y2 = land_array[:,1]
plt.plot(x1, y1, 'bo', x2, y2, 'r+')
plt.xlabel("red")
plt.ylabel("green")
plt.title("Sea or Land option 1")
plt.subplot(132)
x1 = sea_array[:,0]
y1 = sea_array[:,2]
x2 = land_array[:,0]
y2 = land_array[:,2]
plt.plot(x1, y1, 'bo', x2, y2, 'r+')
plt.xlabel("red")
plt.ylabel("blue")
plt.title("Sea or Land option 2")
plt.subplot(133)
x1 = sea_array[:,1]
y1 = sea_array[:,2]
x2 = land_array[:,1]
y2 = land_array[:,2]
plt.plot(x1, y1, 'bo', x2, y2, 'r+')
plt.xlabel("green")
plt.ylabel("blue")
plt.title("Sea or Land option 3")
plt.show()
