from django.shortcuts import render
from Face_Analysis import models
from face_token import result

# Create your views here.
def add_face_data(request):
    if request.method == "POST":

        lefteyex = request.POST.get("lefteyex", None)
        lefteyey = request.POST.get("lefteyey", None)
        rihgteyex = request.POST.get("rihgteyex", None)
        rihgteyey = request.POST.get("rihgteyey", None)
        rotation = request.POST.get("rotation", None)
        distance = request.POST.get("distance", None)
        ratio = request.POST.get("ratio", None)

        models.f_change_data.objects.create(
            lefteyex=lefteyex,
            lefteyey=lefteyey,
            rihgteyex=rihgteyex,
            rihgteyey=rihgteyey,
            rotation = rotation,
            distance = distance,
            ratio = ratio,
            )


        face_data = models.f_change_data.objects.all()

    #return render(request, 'seethings.html',{'thingname':thingname,'find_place':find_place})
    return render(request, 'analysis.html', {"face_data":face_data})

def get_photos (request) :
    return render(request,'Getphotos.html')

def face_analysis (request) :
    return render(request,'Analysis.html')