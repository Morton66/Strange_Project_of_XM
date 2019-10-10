from PIL import Image,ImageFilter,ImageDraw,ImageFont
import cv2
import numpy as np
#m=open("avatar.jpg","rb+")
m=cv2.imread('1.jpg')
mf=open('read.txt','w+')
width=960
height=953
f=[]
p=[]
mm=0;
print(m[0,0,1])
for i in range(width):
	
	for j in range(height):
		p.append(m[j,i,0])
		#p.append(',')
		p.append(m[j,i,1])
		#p.append(',')
		p.append(m[j,i,2])
		#print(p)
		f.append(str(p))
		p=[]
#print(f[0])
#mf.write('I Love')
#mf.flush()
np.save("data.txt",f)
with open("data.txt","w+") as q:
	for i in f:
#		if mm%3==0 and mm!=0:
#			q.write('\n')
#		mm+=1
		q.write('\n')
		q.write(i)
	#print(f.readline())
#print(m)
