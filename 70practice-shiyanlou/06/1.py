实际程序见crack.py, 此程序是说明、实验

#-*- coding:utf8 -*-
from PIL import Image  # http://pillow.readthedocs.io/en/latest/reference/Image.html?highlight=convert

im = Image.open("captcha.gif")


#(将图片转换为8位像素模式)
im.convert("P")
#打印颜色直方图
print im.histogram()
im.show()


his = im.histogram()
values = {}
for i in range(256):
    values[i] = his[i]
# 对给定的List L进行排序，方法1.用List的成员函数sort进行排序;方法2.用built-in函数sorted进行排序（从2.4开始）
for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
    print j,k


im2 = Image.new("P",im.size,255)
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227: # these are the numbers to get
            im2.putpixel((y,x),0)
#im2.show()
print im2.size[0] #图片的长
print im2.size[1] #图片的高


#找出字符的纵向范围：（得到每个字符开始和结束的列序号。）
inletter = False
foundletter=False
start = 0
end = 0
letters = []
for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y
    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))
    inletter=False
print letters


#每个字符切割成单独的图片：
import hashlib
import time
count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    m.update("%s%s"%(time.time(),count)) #用时间+序号的md5生成个文件名
    im3.save("./%s.gif"%(m.hexdigest()))
    count += 1



# 在这里我们使用向量空间搜索引擎来做字符识别，它具有很多优点：
#
#     不需要大量的训练迭代
#     不会训练过度
#     你可以随时加入／移除错误的数据查看效果
#     很容易理解和编写成代码
#     提供分级结果，你可以查看最接近的多个匹配
#     对于无法识别的东西只要加入到搜索引擎中，马上就能识别了。
#
# 当然它也有缺点，例如分类的速度比神经网络慢很多，它不能找到自己的方法解决问题等等。
# 关于向量空间搜索引擎的原理可以参考这篇文章：http://ondoc.logand.com/d/2697/pdf
# Don't panic。向量空间搜索引擎名字听上去很高大上其实原理很简单。拿文章里的例子来说：
# 你有 3 篇文档，我们要怎么计算它们之间的相似度呢？2 篇文档所使用的相同的单词越多，那
# 这两篇文章就越相似！但是这单词太多怎么办，就由我们来选择几个关键单词，选择的单词又被
# 称作特征，每一个特征就好比空间中的一个维度（x，y，z 等），一组特征就是一个矢量，每一
# 个文档我们都能得到这么一个矢量，只要计算矢量之间的夹角就能得到文章的相似度了。


#用 Python 类实现向量空间：
import math
class VectorCompare:
    #计算矢量大小
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.iteritems():
            total += count ** 2
        return math.sqrt(total)
    #计算矢量之间的 cos 值
    def relation(self,concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.iteritems():
            if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))



