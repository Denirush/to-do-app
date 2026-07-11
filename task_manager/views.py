from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import TaskList
from django.contrib.auth import get_user_model
from .forms import TaskForm,UserForm
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()
def sign_up(req):
    if req.method =='POST':
            form = UserForm(req.POST)
            if form.is_valid():
                  user = form.save(commit=False)
                  user.set_password(form.cleaned_data['password1'])
                  user.save()
                  login(req,user)
                  return redirect('home')
    else:
          form =UserForm()
    return render(req,'signup.html',{'form':form})

@login_required
def log_out(req):
    
      logout(req)
      return redirect('login')

def log_in(req):
    form = AuthenticationForm(req, data=req.POST or None)

    if req.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('home')

    return render(req, 'login.html', {'form': form})

@login_required
def home(req):
    tasks = TaskList.objects.filter(user=req.user)
    return render(req,'home.html',{'tasks':tasks})


@login_required
def create(req):
     if req.method=='POST':
           form =TaskForm(req.POST)
           if form.is_valid():
                 task = form.save(commit=False)
                 task.user=req.user
                 task.save()
                 return redirect('home')
     else:
           form =TaskForm()
     return render(req,'create.html',{'form':form})

@login_required
def toggle(req,pk):
      if req.method=='POST':
          
                  task = get_object_or_404(TaskList,pk =pk,user=req.user)
                  task.completed= not task.completed
                  task.save()
                  return redirect('home')
      
      return redirect('home')
            
@login_required
def delete(req,pk):
      if req.method=='POST':
            task = get_object_or_404(TaskList,pk=pk,user=req.user)
            task.delete()
      return redirect('home')