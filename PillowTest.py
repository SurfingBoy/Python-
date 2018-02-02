# from PIL import Image,ImageFilter
#
# #打开一个jpg文件
# im = Image.open('C:/Users/su/Pictures/图片1.jpg')
# #获取图片的尺寸
# w,h=im.size
# print('Original image size:%sx%s'%(w,h))
# #缩放到50%
# im.thumbnail((w//2,h//2))
# print('Resize image to:%sx%s'%(w//2,h//2))
# #应用模糊滤镜
# im2=im.filter(ImageFilter.BLUR)
# #保存图片
# im.save('hhh.jpg','jpeg')
# im2.save('blur.jpg','jpeg')

#--------------图片验证码---------------
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))  #ASCII码表A-Z
#随机颜色（背景）
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色（文字）
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建font对象
font=ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',36)
#创建draw对象
draw=ImageDraw.Draw(image)
#填充背景每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输出文字
for t in range(4):
    draw.text((60*t+15,10),rndChar(),fill=rndColor2(),font=font)
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
#--------------图片验证码---------------