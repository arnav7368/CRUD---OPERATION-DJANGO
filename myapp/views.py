from django.shortcuts import render,HttpResponseRedirect
from django.db.models import Q
from .models import Employee

def index(request):
    data=Employee.objects.all()
    return render(request,'index.html',{"data":data})

def add(request):
    if(request.method=="POST"):
        e=Employee()
        e.name=request.POST.get("name")
        e.email=request.POST.get("email")
        e.phone=request.POST.get("phone")
        e.dsg=request.POST.get("dsg")
        e.salary=request.POST.get("salary")
        e.city=request.POST.get("city")
        e.state=request.POST.get("state")
        e.save()
        return HttpResponseRedirect("/")
    return render(request,'add.html')

def delete(request,id):
    try:
        data=Employee.objects.get(id=id)
        data.delete()
    except:
        pass
    return HttpResponseRedirect("/")

def edit(request,id):
    try:
        data=Employee.objects.get(id=id)
        if(request.method=="POST"):
            data.name=request.POST.get("name")
            data.email=request.POST.get("email")
            data.phone=request.POST.get("phone")
            data.dsg=request.POST.get("dsg")
            data.salary=request.POST.get("salary")
            data.city=request.POST.get("city")
            data.state=request.POST.get("state")
            data.save()
            return HttpResponseRedirect("/")
        return render(request,"edit.html",{"data":data})
    except:
        pass
    return HttpResponseRedirect("/")

def search(request):
    if(request.method=="POST"):
        search=request.POST.get("search")
        # filter(name__icontains=search)
        data=Employee.objects.filter(Q(name__icontains=search)|
                                     Q(city__icontains=search)|
                                     Q(state__icontains=search)|
                                     Q(email__icontains=search)|
                                     Q(phone__icontains=search)|
                                     Q(dsg__icontains=search))
        return render(request,'index.html',{"data":data})
    else:
        return HttpResponseRedirect("/")

