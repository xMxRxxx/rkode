from .models import BlogModel
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger

# Create your views here.
def home(request):
	return render(request, 'home.html')

def home_Programing(request,tipe):
	if tipe == "C":
		data=BlogModel.objects.filter(category="P",sub_category="C")
		pagig = Paginator(data,per_page=2)
		page_number = request.GET.get('page')
		page_object = pagig.get_page(page_number)
		print(data)
		return render(request, 'programing/home.html',{'data':page_object})
	elif tipe == "CPP":
		data=BlogModel.objects.filter(category="P",sub_category="CPP")
		
		return render(request, 'programing/home.html',{'data':data})
	elif tipe == "JV":
		data=BlogModel.objects.filter(category="P",sub_category="JV")
		
		return render(request, 'programing/home.html',{'data':data})
	elif tipe == "PY":
		data=BlogModel.objects.filter(category="P",sub_category="PY")
		
		return render(request, 'programing/home.html',{'data':data})
	elif tipe == "FL":
		data=BlogModel.objects.filter(category="P",sub_category="FL")
		
		return render(request, 'programing/home.html',{'data':data})
	else:
		return render(request, 'soon.html')

def detail_Programing(request,tipe,slug):
	if tipe == "C":
		data=BlogModel.objects.filter(category="P",sub_category="C")
		data1=BlogModel.objects.filter(category="P",sub_category="C",slug=slug)
		ttl = ["C PROGRAMING TUTORIAL"]
		print(data)
		return render(request, 'programing/detail.html',{'data':data,'data1':data1,'ttl':ttl })
	else:
		return render(request, 'soon.html')


def home_Project(request,tipe):
	if tipe == "C":
		data=BlogModel.objects.filter(category="PR",sub_category="C")
		pagig = Paginator(data,per_page=2)
		page_number = request.GET.get('page')
		page_object = pagig.get_page(page_number)
		print(data)
		return render(request, 'programing/home.html',{'data':page_object})
	elif tipe == "CPP":
		data=BlogModel.objects.filter(category="PR",sub_category="CPP")
		
		return render(request, 'programing/home.html',{'data':data})
	elif tipe == "JV":
		data=BlogModel.objects.filter(category="PR",sub_category="JV")
		
		return render(request, 'programing/home.html',{'data':data})
	elif tipe == "PY":
		data=BlogModel.objects.filter(category="PR",sub_category="PY")
		
		return render(request, 'programing/home.html',{'data':data})
	elif tipe == "FL":
		data=BlogModel.objects.filter(category="PR",sub_category="FL")
		
		return render(request, 'programing/home.html',{'data':data})
	else:
		return render(request, 'soon.html')

def detail_Project(request,tipe,slug):
	if tipe == "C":
		data=BlogModel.objects.filter(category="PR",sub_category="C")
		data1=BlogModel.objects.filter(category="PR",sub_category="C",slug=slug)
		ttl = ["C PROJECT TUTORIAL"]
		print(data)
		return render(request, 'programing/detail.html',{'data':data,'data1':data1,'ttl':ttl })
	else:
		return render(request, 'soon.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def register_view(request):
    return render(request , 'register.html')



def verify(request,token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')