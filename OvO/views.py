from django.shortcuts import render_to_response,render
import urllib3,base64,json
from urllib import urlencode
from Face_Analysis.access_token import key

def home(request):
    return render_to_response('home.html')

def Wear_Glass(request):
    if request.method == 'GET':
        return render_to_response('Wear_glass.html')

def Getphotos(request):
    if request.method == 'GET':
        return render_to_response('Getphotos.html')
    if request.method == 'POST':
        imgurl = request.POST.get('cameraInput')
        print(imgurl)
        access_token = key
        http = urllib3.PoolManager()
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=' + access_token

        f = open('image.jpg','rb')
        img = base64.b64encode(f.read())
        # params={'image':''+str(img)+'','image_type':'BASE64','max_face_num':'10','face_field':'type,age,faceshape,gender','face_type':'LIVE',}
        params = {'image': '' + str(img) + '', 'image_type': 'BASE64',
                  'face_field': 'type,age,faceshape,gender,landmark', 'face_type': 'LIVE', }
        # params={'image':'6537be97c7032e31efecc75a973d9b92','image_type':'FACE_TOKEN','face_field':'age,beauty,faceshape,gender,glasses'}
        # params={'image':'http://www.testing.com/face(1).jpg','image_type':'BASE64','face_field':'age,beauty,faceshape,gender,glasses'}
        # params={'image':'E:\projects\ovo\aip\face.jpg','image_type':'BASE64','face_field':'age,beauty,faceshape,gender,glasses'}

        params = urlencode(params)
        request = http.request('POST',
                               url,
                               body=params,
                               headers={'Content-Type': 'application/json'})

        result = str(request.data)
        print(result)
        udict = json.loads(result)
        print udict
        return render(request,'Getphotos.html',result)
