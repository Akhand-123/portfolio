from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact,Blog,Internship

# Create your views here.
def home(request):
    return render(request,'home.html')

def handleblog(request):
    posts=Blog.objects.all()
    context={"posts":posts}    
    return render(request,'handleblog.html',context)

def about(request):
    return render(request,'about.html')

def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please login to access this page")
        return redirect('/auth/login/')
    if request.method == 'POST':
        fname = request.POST.get('name')
        fusn = request.POST.get('usn')
        femail = request.POST.get('email')
        fcollage = request.POST.get('cname')
        foffer = request.POST.get('offer')
        fstartdate = request.POST.get('startdate')
        fenddate = request.POST.get('enddate')
        fprojreport = request.POST.get('projreport')
        
        # converting to the upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcollage=fcollage.upper()
        foffer=foffer.upper()
        
        # check details
        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)
        
        if check1 or check2:
            messages.warning(request,"Your details are stored already!")
            return redirect('/internshipdetails')
        
        query=Internship(fullname=fname,usn=fusn,email=femail,collage_name=fcollage,offer_status=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fprojreport)
        query.save()
        messages.success(request,"Form is submitted successfully!")
        return redirect('/internshipdetails')
    return render(request,'internship.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fnumber = request.POST.get('num')
        fdescription = request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fnumber,description=fdescription)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get back you soon!")
        
        return redirect('/contact')
    
    return render(request,'contact.html')