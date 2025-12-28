from django.shortcuts import render
from app.forms import Signupform


def signup(request):
    if (request.method=='GET'):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'signup.html',context)
    
    if (request.method=='POST'):

        # submitted data
        print(request.POST)

        # create form_instance with submitted data
        form_instance =Signupform(request.POST)

        # checks validity of data
        if (form_instance.is_valid()):
            data=form_instance.cleaned_data
            print(data)
            username=data['username']
            password=data['password']
            email=data['email']
            phone=int(data['phone'])
            age=int(data['age'])
            gender=data['gender']
            context={'form':form_instance}
            return render(request,'signup.html',context)


        # process the data
        # print(data)

