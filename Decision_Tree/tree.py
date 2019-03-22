# -*- coding: UTF-8 -*-


def facemode(face):                                                             #这里为脸部识别的最初始函数
    if face == 0:                                                               #输入不同的数字进入不同的脸型函数
        print '您是长下巴还是宽下巴？'
        finall = jawlength1()
    if face == 1:
        finall=yuanlian()
    if face == 2:
        finall = fanglian()
    if face == 3:
        finall = xinlian()
    if face == 4:
        finall = sanjiaolian()
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



def jawlength1():
    length = input('请输入下巴长度:')                                                      #长宽下巴的部分
    if length == 0:
        return yuanlian()
    if length == 1:
        return 100;




def jawlength2():
    length = input('请输入下巴宽度:')                                                                       #宽窄下巴的部分
    if length == 0:
        return 0
    if length == 1:
        return 1



def yuanlian():
    sex = rsex()                                                                                    #圆脸的函数
    age = rage()
    chara = character(sex, age)
    return chara+100



def character(sex,age):
    if sex ==1 & age == 0:                                                                             #非心形脸和三角脸的性格函数
        print '你是个文静的女孩儿还是个个性而又奔放的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 6
        if chara == 1:
            return 7
    if sex == 1 & age == 1:
        print '你是个优雅文静的女孩儿还是个开朗时尚的女孩儿还是个干练成熟的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 8
        if chara == 1:
            return 9
        if chara == 2:
            return 10
    if sex == 1 & age == 2:
        print '你是个优雅文静的女孩儿还是个开朗时尚的女孩儿还是个干练成熟的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 8
        if chara == 1:
            return 9
        if chara == 2:
            return 10
    if sex == 0 & age == 0:
        print '你是个安静的男孩还是个个性时尚的男孩呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 1
        if chara == 1:
            return 2
    if sex == 0 & age == 1:
        print '你是个优雅文静的男孩儿还是个开朗时尚的男孩儿还是个干练成熟的男孩儿呢？'
        if chara == 0:
            return 3
        if chara == 1:
            return 4
        if chara == 2:
            return 5
    if sex == 0 & age == 2:
        print '你是个优雅文静的男孩儿还是个开朗时尚的男孩儿还是个干练成熟的男孩儿呢？'
        if chara == 0:
            return 3
        if chara == 1:
            return 4
        if chara == 2:
            return 5





def character1(sex,age):
    if sex == 1 & age == 0:                                                                 #心形脸和三角脸的性格函数
        print '你是个文静的女孩儿还是个个性而又奔放的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            jaw = jawlength2()
            if jaw == 0:
                return 6
            if jaw==1:
                return 7
        if chara == 1:
            return 8
    if sex == 1 &age == 1:
        print '你是个优雅文静的女孩儿还是个开朗时尚的女孩儿还是个干练成熟的女孩儿呢？'
        chara = input('请输入性格')
        if chara == 0:
            return 9
        if chara == 1:
            return 10
        if chara == 2:
            return 11
    if sex == 1 & age == 2:
        print '你是个优雅文静的女孩儿还是个开朗时尚的女孩儿还是个干练成熟的女孩儿呢？'
        chara = input ('请输入性格')
        if chara == 0:
            return 9
        if chara == 1:
            return 10
        if chara == 2:
            return 11
    if sex == 0 & age == 0:
        print '你是个安静的男孩还是个个性时尚的男孩呢？'
        chara=input('请输入性格')
        if chara == 0:
            jaw=jawlength2()
            if jaw == 0:
                return 0
            if jaw == 1:
                return 1
        if chara == 1:
            return 2
    if sex == 0 & age == 1:
        print '你是个优雅文静的男孩儿还是个开朗时尚的男孩儿还是个干练成熟的男孩儿呢？'
        if chara == 0:
            return 3
        if chara == 1:
            return 4
        if chara == 2:
            return 5
    if sex == 0 & age == 2:
        print '你是个优雅文静的男孩儿还是个开朗时尚的男孩儿还是个干练成熟的男孩儿呢？'
        if chara == 0:
            return 3
        if chara == 1:
            return 4
        if chara == 2:
            return 5





def fanglian():
    sex = rsex()
    age = rage()
    chara = character(sex, age)
    return chara+200


def xinlian():
    sex = rsex()
    age = rage()
    chara = character1(sex,age)
    return chara+300


def sanjiaolian():
    sex = rsex()
    age = rage()
    chara = character1(sex,age)
    return chara+400




number = input('请输入你的脸型')
print facemode(number)