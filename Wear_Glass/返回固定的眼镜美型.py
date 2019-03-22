# -*- coding: UTF-8 -*-
import urllib3,base64
import urllib, urllib2, sys
import ssl
import urllib
import json
from PIL import Image




def facemode(face,age,jaw,sex):                                                             #这里为脸部识别的最初始函数
    if face == 0:                                                               #输入不同的数字进入不同的脸型函数
        print '您是长下巴还是宽下巴？'
        finall = jawlength1(age,jaw,sex)
    if face == 1:
        finall=yuanlian(age,sex)
    if face == 2:
        finall = fanglian(age,sex)
    if face == 3:
        finall = xinlian(age,jaw,sex)
    if face == 4:
        finall = sanjiaolian(age,jaw,sex)
    return finall



def rsex():
    sex=input('请输入性别:')                                                                 #获取性别函数
    if sex == 0:
        return 0
    if sex == 1:
        return 1



def rage():
    age = input('你今年多大了？')                                                              #获取年龄部分
    if age <= 18:
        return 0
    if age > 18 & age <= 35:
        return 1
    if age > 35:
        return 2



def jawlength1(age,jaw,sex):                                                #长宽下巴的部分
    if jaw == 0:
        return yuanlian(age,sex)
    if jaw == 1:
        return 100;




def jawlength2():
    length = input('请输入下巴宽度:')                                                                       #宽窄下巴的部分
    if length == 0:
        return 0
    if length == 1:
        return 1



def yuanlian(age,sex):
    chara = character(sex, age)
    return chara+100



def character(sex,age):
    if sex ==1 & age == 0:                                                                             #非心形脸和三角脸的性格函数
        print '你是个文静的女孩儿还是个个性而又奔放的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 51
        if chara == 1:
            return 52
    if sex == 1 & age == 1:
        print '你是个优雅文静的女孩儿还是个开朗时尚的女孩儿还是个干练成熟的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 53
        if chara == 1:
            return 54
        if chara == 2:
            return 55
    if sex == 1 & age == 2:
        print '你是个优雅文静的女孩儿还是个开朗时尚的女孩儿还是个干练成熟的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 1:
            return 56
        if chara == 2:
            return 57
    if sex == 0 & age == 0:
        print '你是个安静的男孩还是个个性时尚的男孩呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 1
        if chara == 1:
            return 2
    if sex == 0 & age == 1:
        print '你是个优雅文静的男孩儿还是个开朗时尚的男孩儿还是个干练成熟的男孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 3
        if chara == 1:
            return 4
        if chara == 2:
            return 5
    if sex == 0 & age == 2:
        print '你是个优雅文静的男孩儿还是个开朗时尚的男孩儿还是个干练成熟的男孩儿呢？'
        chara = input('请输入性格')
        if chara == 1:
            return 6
        if chara == 2:
            return 7





def character1(sex,jaw,age):
    if sex == 1 & age == 0:                                                                 #心形脸和三角脸的性格函数
        print '你是个文静的女孩儿还是个个性而又奔放的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            if jaw == 1:
                return 51
            if jaw==0:
                return 52
        if chara == 1:
            return 53
    if sex == 1 & age == 1:
        print '你是个优雅文静的女孩儿还是个开朗时尚的女孩儿还是个干练成熟的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 54
        if chara == 1:
            return 55
        if chara == 2:
            return 56
    if sex == 1 & age == 2:
        print '你是个优雅文静的女孩儿还是个开朗时尚的女孩儿还是个干练成熟的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 57
        if chara == 1:
            return 58
    if sex == 0 & age == 0:
        print '你是个安静的男孩还是个个性时尚的男孩呢？'
        chara = input('请输入性格')
        if chara == 0:
            if jaw == 1:
                return 1
            if jaw == 0:
                return 2
        if chara == 1:
            return 3
    if sex == 0 & age == 1:
        print '你是个优雅文静的男孩儿还是个开朗时尚的男孩儿还是个干练成熟的男孩儿呢？'
        if chara == 0:
            return 4
        if chara == 1:
            return 5
        if chara == 2:
            return 6
    if sex == 0 & age == 2:
        print '你是个优雅文静的男孩儿还是个开朗时尚的男孩儿还是个干练成熟的男孩儿呢？'
        if chara == 0:
            return 7
        if chara == 1:
            return 8





def fanglian(age,sex):
    chara = character(sex, age)
    return chara+200


def xinlian(age,jaw,sex):
    chara = character1(sex,jaw,age)
    return chara+300


def sanjiaolian(age,jaw,sex):
    chara = character1(sex,jaw,age)
    return chara+400


def wearglass(request):

    img64 = request.POST.get('imgurl')
    imgdata = base64.b64decode(img64)
    img1 = open('1.jpg', 'wb')
    img1.write(imgdata)
    access_token = key
    http=urllib3.PoolManager()
    url='https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token='+access_token
    params={'image':''+str(img64)+'','image_type':'BASE64','face_field':'age,faceshape,gender,landmark'}
    params=urllib.urlencode(params)
    request=http.request('POST',
                          url,
                          body=params,
                          headers={'Content-Type':'application/json'})
    print (request.data)
    params = json.loads(request.data)
    lianxing=params['result']['face_list'][0]['face_shape']['type']


    if lianxing == "oval":
        lian=0
    if lianxing == "round":
         lian = 1
    if lianxing == "square":
        lian = 2
    if lianxing == "heart":
        lian = 3
    if lianxing == "triangle":
        lian = 4


    stringsex = params['result']['face_list'][0]['gender']['type']


    if stringsex == "female":
        sex=1
    if stringsex=="male":
        sex=0


    age=params['result']['face_list'][0]['age']
    print ("您的年龄是否是%d"%(age-2))


    if age <= 18:
        age= 0
    if age > 18 & age <= 35:
        age= 1
    if age > 35:
        age= 2


    left_nose = params['result']['face_list'][0]['landmark72'][50]['y']
    right_nose = params['result']['face_list'][0]['landmark72'][51]['y']
    nose_low =  (right_nose + left_nose)/2

    jaw = params['result']['face_list'][0]['landmark72'][5]['y']
    renzhong = nose_low - jaw
    standard = renzhong/2
    user_jaw = params['result']['face_list'][0]['landmark72'][63]['y'] - params['result']['face_list'][0]['landmark72'][5]['y']



    if standard > user_jaw:
        jaw = 1
    else:
        jaw = 0
    mark=facemode(lian,age,jaw,sex)
    print facemode(lian,age,jaw,sex)
    print (request.data)
    result = str(request.data)
    finallresult=json.loads(result)
    lefteyex=finallresult['result']['face_list'][0]['landmark'][0]['x']
    lefteyey=finallresult['result']['face_list'][0]['landmark'][0]['y']
    righteyex=finallresult['result']['face_list'][0]['landmark'][1]['x']
    righteyey=finallresult['result']['face_list'][0]['landmark'][1]['y']
    rotation=finallresult['result']['face_list'][0]['location']['rotation']
    facepoint=finallresult['result']['face_list'][0]['landmark72']
    print facepoint[0]['x']
    print lefteyex
    print lefteyey
    print righteyex
    print righteyey
    print rotation
    distance=righteyex-lefteyex
    img1=img1.rotate(rotation)
    glass=Image.open(str(mark)+'.png')
    (x,y) = glass.size
    ratio=distance/(glass.size[0]/2.14)
    print glass.size[0]
    x_s = int(glass.size[0]*ratio)
    y_s = y*x_s/x
    out=glass.resize((x_s,y_s),Image.ANTIALIAS)
    placex=int((lefteyex+righteyex)/2-(out.size[0]/2))
    placey=int((lefteyey+righteyey)/2-(out.size[1]/2))
    img1.paste(out,(placex,placey+15),mask=out)
    img1.show()