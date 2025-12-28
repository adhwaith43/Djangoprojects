from django.shortcuts import render
from form.forms import AdditionForm,BMIForm,FactForm

def home(request):
    if (request.method=='GET'):
        return render(request,'home.html')

def addition(request):
    if (request.method=='GET'):
        form_instance=AdditionForm()
        context={'form':form_instance}
        return render(request,'addition.html',context)
    
    if (request.method=='POST'):

        # submitted data
        print(request.POST)

        # create form_instance with submitted data
        form_instance =AdditionForm(request.POST)

        # checks validity of data
        if (form_instance.is_valid()):
            data=form_instance.cleaned_data
            print(data)
            n1=int(data['num1'])
            n2=int(data['num2'])
            s=n1+n2
            context={'result':s,'form':form_instance}
            return render(request,'addition.html',context)


        # process the data
        # print(data)


        return render(request,'addition.html')
    
def bmi(request):
    if (request.method=='GET'):
        form_instance=BMIForm()
        context={'form':form_instance}
        return render(request,'bmi.html',context)
    
    if (request.method=='POST'):

        # submitted data
        print(request.POST)

        # create form_instance with submitted data
        form_instance =BMIForm(request.POST)

        # checks validity of data
        if (form_instance.is_valid()):
            data=form_instance.cleaned_data
            print(data)
            w=int(data['weight'])
            h=int(data['height'])
            s=w/((h/100)**2)
            context={'result':s,'form':form_instance}
            return render(request,'bmi.html',context)


        # process the data
        # print(data)



def fact(request):
    if (request.method=='GET'):
        form_instance=FactForm()
        context={'form':form_instance}
        return render(request,'fact.html',context)
    
    if (request.method=='POST'):

        # submitted data
        print(request.POST)

        # create form_instance with submitted data
        form_instance =FactForm(request.POST)

        # checks validity of data
        if (form_instance.is_valid()):
            data=form_instance.cleaned_data
            print(data)
            num1=int(data['num1'])
            s=1
            for i in range(1,num1+1):
                s*=i
            context={'result':s,'form':form_instance}
            return render(request,'fact.html',context)


        # process the data
        # print(data)

