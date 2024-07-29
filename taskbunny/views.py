from django.shortcuts import render,redirect,HttpResponse
from taskbunny.forms import MyUserForm,LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate
from taskbunny.models import OtherProileData,Task
from rest_framework.views import APIView

# Create your views here.
def login_view(request):
    if( request.method=="POST"):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                redirect('home')
            # username =
    else:
        form =  LoginForm()
    return render(request,'login.html',{'form':form})

@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        form  = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            user = authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
            # return redirect('login')
        else:
            HttpResponse("input is not valid")
    else:
        form = MyUserForm()
    return render(request,'signup.html',{'form':form})

def home_view(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        tasks = Task.objects.filter(user=user)
        print(tasks)
        return render(request,'home.html',{'tasks':tasks})
    return redirect('login')

def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        otherProfileInfo = OtherProileData.objects.get(user=user)
        return render(request,'profile.html',context={'profile':user,'otherInfo':otherProfileInfo})
    return redirect('login')


# Rest APIs
# class TaskView(APIView):
#     def post(self,request):
#         title = request.POST.get('title','')
#         description = request.POST.get('description','')
        
#         return HttpResponse("Task Created succesfully")
#     def update(self,request):
#         return HttpResponse("Task updated succesfully")
def createTask(request):
    title = request.POST.get('title','')
    description = request.POST.get('description','')
    user = request.user
    taskObj = Task()
    taskObj.user=user
    taskObj.title=title
    taskObj.description=description
    taskObj.save()
    return redirect('home')

def updateTask(request):
    title = request.POST.get('title','')
    description = request.POST.get('description','')
    user = request.user
    taskObj = Task()
    taskObj.user=user
    taskObj.title=title
    taskObj.description=description
    taskObj.save()
    return redirect('home')