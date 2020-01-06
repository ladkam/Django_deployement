from django.shortcuts import render,redirect
from django.http import HttpResponse
from apptwo.models import user
from apptwo.forms import UserForm

# Create your views here.

def index(request):
    return HttpResponse("<em>My second app</em>")

def help_page(request):
    my_dict={'help_text':'I can help','help_title':'Help'}
    return render(request,'help.html',context=my_dict)



def Users(request):
    UserList = user.objects.all()
    my_dict={'Users':UserList}
    return render(request,'Users.html',context=my_dict)

def signin(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            # NewUser = user(FirstName = form.cleaned_data['FirstName'],LastName=form.cleaned_data['LastName'],email=form.cleaned_data['email'])
            # NewUser.save()
            return redirect('Users')
    return render(request,'signin.html',{'form':form})
