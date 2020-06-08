from django.shortcuts import render

def name_view(request):
    return render(request,'myapp/name.html')

def process_name_view(request):
    name=request.GET['name']
    response=render(request,'myapp/age.html',{'name':name})
    response.set_cookie('name',name,max_age=180)
    return response #return respone with cookie

def process_age_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    response=render(request,'myapp/gf.html',{'name':name})
    response.set_cookie('age',age,max_age=180)
    return response

def results_view(request):
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    gfn=request.GET['gfn']
    response=render(request,'myapp/results.html',{'name':name,'age':age,'gfn':gfn})
    response.set_cookie('gfn',gfn,max_age=180)
    return response

