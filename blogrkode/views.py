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
	try:
		if tipe == "C":
			data=BlogModel.objects.filter(category="P",sub_category="C")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'programing/home.html',{'data':page_object})
		elif tipe == "CPP":
			data=BlogModel.objects.filter(category="P",sub_category="CPP")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'programing/home.html',{'data':page_object})
		elif tipe == "JV":
			data=BlogModel.objects.filter(category="P",sub_category="JV")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'programing/home.html',{'data':page_object})
		elif tipe == "PY":
			data=BlogModel.objects.filter(category="P",sub_category="PY")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'programing/home.html',{'data':page_object})
		elif tipe == "FL":
			data=BlogModel.objects.filter(category="P",sub_category="FL")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'programing/home.html',{'data':page_object})
		else:
			return render(request, 'soon.html')
	except Exception as e:
		return render(request, 'soon.html')
	

def detail_Programing(request,tipe,slug):
	try:
		if tipe == "C":
			data=BlogModel.objects.filter(category="P",sub_category="C")
			data1=BlogModel.objects.filter(category="P",sub_category="C",slug=slug)
			ttl = ["C PROGRAMING TUTORIAL"]
			
			return render(request, 'programing/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		elif tipe == "CPP":
			data=BlogModel.objects.filter(category="P",sub_category="CPP")
			data1=BlogModel.objects.filter(category="P",sub_category="CPP",slug=slug)
			ttl = ["C++ PROGRAMING TUTORIAL"]
			
			return render(request, 'programing/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		elif tipe == "JV":
			data=BlogModel.objects.filter(category="P",sub_category="JV")
			data1=BlogModel.objects.filter(category="P",sub_category="JV",slug=slug)
			ttl = ["JAVA PROGRAMING TUTORIAL"]
			
			return render(request, 'programing/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		elif tipe == "PY":
			data=BlogModel.objects.filter(category="P",sub_category="PY")
			data1=BlogModel.objects.filter(category="P",sub_category="PY",slug=slug)
			ttl = ["PYTHON PROGRAMING TUTORIAL"]
			
			return render(request, 'programing/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		elif tipe == "FL":
			data=BlogModel.objects.filter(category="P",sub_category="FL")
			data1=BlogModel.objects.filter(category="P",sub_category="FL",slug=slug)
			ttl = ["FLUTTER PROGRAMING TUTORIAL"]
			
			return render(request, 'programing/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		else:
			return render(request, 'soon.html')
	except Exception as e:
		return render(request, 'soon.html')
	


def home_Project(request,tipe):
	try:
		if tipe == "C":
			data=BlogModel.objects.filter(category="PR",sub_category="C")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'project/home.html',{'data':page_object})
		elif tipe == "CPP":
			data=BlogModel.objects.filter(category="PR",sub_category="CPP")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'project/home.html',{'data':data})
		elif tipe == "JV":
			data=BlogModel.objects.filter(category="PR",sub_category="JV")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'project/home.html',{'data':data})
		elif tipe == "PY":
			data=BlogModel.objects.filter(category="PR",sub_category="PY")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'project/home.html',{'data':data})
		elif tipe == "FL":
			data=BlogModel.objects.filter(category="PR",sub_category="FL")
			pagig = Paginator(data,per_page=5)
			page_number = request.GET.get('page')
			page_object = pagig.get_page(page_number)
			return render(request, 'project/home.html',{'data':data})
		else:
			return render(request, 'soon.html')
	except Exception as e:
		return render(request, 'soon.html')
	

def detail_Project(request,tipe,slug):
	try:
		if tipe == "C":
			data=BlogModel.objects.filter(category="PR",sub_category="C")
			data1=BlogModel.objects.filter(category="PR",sub_category="C",slug=slug)
			ttl = ["C PROJECT TUTORIAL"]
			
			return render(request, 'project/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		elif tipe == "CPP":
			data=BlogModel.objects.filter(category="PR",sub_category="CPP")
			data1=BlogModel.objects.filter(category="PR",sub_category="CPP",slug=slug)
			ttl = ["C++ PROGRAMING TUTORIAL"]
			return render(request, 'project/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		elif tipe == "JV":
			data=BlogModel.objects.filter(category="PR",sub_category="JV")
			data1=BlogModel.objects.filter(category="PR",sub_category="JV",slug=slug)
			ttl = ["JAVA PROGRAMING TUTORIAL"]
			return render(request, 'project/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		elif tipe == "PY":
			data=BlogModel.objects.filter(category="PR",sub_category="PY")
			data1=BlogModel.objects.filter(category="PR",sub_category="PY",slug=slug)
			ttl = ["PYTHON PROGRAMING TUTORIAL"]
			return render(request, 'project/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		elif tipe == "FL":
			data=BlogModel.objects.filter(category="PR",sub_category="FL")
			data1=BlogModel.objects.filter(category="PR",sub_category="FL",slug=slug)
			ttl = ["FLUTTER PROGRAMING TUTORIAL"]
			return render(request, 'project/detail.html',{'data':data,'data1':data1,'ttl':ttl })
		else:
			return render(request, 'soon.html')

	except Exception as e:
		return render(request, 'soon.html')
	

# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("main:homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="register.html", context={"register_form":form})

# def register_view(request):
#     return render(request , 'register.html')



# def verify(request,token):
#     try:
#         profile_obj = Profile.objects.filter(token = token).first()
        
#         if profile_obj:
#             profile_obj.is_verified = True
#             profile_obj.save()
#         return redirect('/login/')

#     except Exception as e : 
#         print(e)
    
#     return redirect('/')