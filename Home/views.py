from django.shortcuts import render , redirect
from django.contrib import messages
from Home.models import Contact , About , Privacy , HeadOffice , IndiaOffice , ContactService
from Course.models import Course
# Create your views here.
def home(request):
	messages.success(request , "Welcome To The ENNews")
	allPosts = Course.objects.all()[::-1]
	allPosts = allPosts[:3]
	context = {'allPost':allPosts}
	return render(request , 'home/home.html',context)

def contact(request):
	messages.success(request, "Welcome To The Contact Page")
	# HeadOffice Area 
	Headpost = HeadOffice.objects.all().first()
	context = {'Headpost':Headpost}
	# return redirect(request , 'home/contact.html' , context)
	# return render(request , 'home/contact.html' , conteat)
	# # IndiaOffice Area
	# Indiapost = IndiaOffice.objects.all().first()
	# return render(request , 'home/contact.html' , conteet)
	# # ContactService Area
	# Contactpost = ContactService.objects.all().first()
	# return render(request , 'home/contact.html' , content)
	# context = {'HeadPost':Headpost,'allPostc':Contactpost,'allPosti':Indiapost}

	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']
		content = request.POST['text']

		if len(name) < 5 or len(email) < 10 or len(phone) < 10 or len(content) < 10:
			messages.warning(request , "Fill Contact Form Properly")
		else:
			contact = Contact(name = name , email = email , phone = phone , msg = content)
			contact.save()
			messages.success(request , "Form Successfully Submit ")
	return render(request , 'home/contact.html')

def about(request):
	# messages.success(request , "Welcome To The About Us ")
	allPosts = About.objects.all().first()
	context = {'allPost': allPosts}
	return render(request , "home/about.html" , context)


def privacy(request):
	# messages.success(request , "Welcome To The Privacy Policy ")
	allPosts = Privacy.objects.all().first()
	context = {'allPost': allPosts}
	return render(request , "home/privacy.html" , context)




def login(request):
	return render(request, 'home/login.html')	