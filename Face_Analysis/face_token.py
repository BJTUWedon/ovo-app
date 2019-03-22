# encoding:utf-8

import urllib3
urllib3.disable_warnings()
from urllib import urlencode
import json
from access_token import key
import time
from django.http import HttpResponse, JsonResponse
# print(key)
def face_token(request):
    time.sleep(5)
    img64 = request.POST.get('imgurl')
    access_token = key
    http=urllib3.PoolManager()
    url='https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token='+access_token
    # f = open(imgurl,'rb') #url由前端提供
    # img = base64.b64encode(f.read())
    #params={'image':''+str(img)+'','image_type':'BASE64','max_face_num':'10','face_field':'type,age,faceshape,gender','face_type':'LIVE',}
    params={'image':''+str(img64[23:])+'','image_type':'BASE64','face_field':'type,age,faceshape,gender,landmark,beauty','face_type':'LIVE',}
    #params={'image':'6537be97c7032e31efecc75a973d9b92','image_type':'FACE_TOKEN','face_field':'age,beauty,faceshape,gender,glasses'}
    #params={'image':'http://www.testing.com/face(1).jpg','image_type':'BASE64','face_field':'age,beauty,faceshape,gender,glasses'}
    #params={'image':'E:\projects\ovo\aip\face.jpg','image_type':'BASE64','face_field':'age,beauty,faceshape,gender,glasses'}

    params=urlencode(params)
    request=http.request('POST',
                          url,
                          body=params,
                          headers={'Content-Type':'application/json'})


    result = str(request.data)
    print(result)
    udict = json.loads(result)
    print udict
    lefteyex = udict['result']['face_list'][0]['landmark'][0]['x']
    lefteyey = udict['result']['face_list'][0]['landmark'][0]['y']
    righteyex = udict['result']['face_list'][0]['landmark'][1]['x']
    righteyey = udict['result']['face_list'][0]['landmark'][1]['y']
    rotation = udict['result']['face_list'][0]['location']['rotation']
    facepoint = udict['result']['face_list'][0]['landmark72'][0]['x']

    # # #要返回页面的数据
    face_width = int(udict['result']['face_list'][0]['location']['width'])
    face_height = int(udict['result']['face_list'][0]['location']['height'])
    face_type = udict['result']['face_list'][0]['face_shape']['type']
    beauty = int(udict['result']['face_list'][0]['beauty'])+15
    datajson = {"face_width": face_width, "face_height": face_height, "face_type": face_type, "beauty": beauty}
    # print (datajson)
    return JsonResponse(datajson)




