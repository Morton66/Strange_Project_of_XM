from PIL import Image

x = 960    #x坐标  通过对txt里的行数进行整数分解
y = 953    #y坐标  x * y = 行数

im = Image.new("RGB", (x, y))   #创建图片
file = open('data.txt')    #打开rbg值的文件

#通过每个rgb点生成图片
#l=file.readline()
#r=l.split(', ')
#print(l)
#print(r[2])
for i in range(0, x):
    for j in range(0, y):
        line = file.readline()  #获取一行的rgb值
       
        rgb = line.split(", ")  #分离rgb，文本中逗号后面有空格
      
        im.putpixel((i, j), (int(rgb[2]), int(rgb[2]), int(rgb[2])))    #将rgb转化为像素

im.show()   #也可用im.save('flag.jpg')保存下来