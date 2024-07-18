from django.shortcuts import redirect,render
from django.http import FileResponse, HttpResponse
from django.conf import settings
from Portfolio.contactform.models import *
from Portfolio.Portfolio.forms import *
from django.core.mail import send_mail
from Portfolio.project.models import *
from Portfolio.Aboutme.models import *
from Portfolio.Services.models import *
from Portfolio.pricing.models import *
from Portfolio.Resume.models import *
from Portfolio.MySkills.models import *
from Portfolio.GetinTouch.models import *
from Portfolio.personalinfo.models import *
import os


def homepage(request):
    form1=ContactForm(request.POST)
    Bannerdata=Banner.objects.all()
    Socialmedia_Postdata=Socialmedia_Post.objects.all()
    Manipulationdata=Manipulation.objects.all()
    Web_Developmentdata=Web_Development.objects.all()
    recentpost = Socialmedia_Post.objects.all()[:6]
    recentwebsite = Web_Development.objects.all().latest('id')
    biodata=bio.objects.all()[:1]
    infodata=info.objects.all()[:1]
    servicedata=service.objects.all()
    pricedata=Price.objects.all()
    for price in pricedata:
         price.services_list = price.services.split(',')
    resumedata=resume.objects.all() 
    Designdata=Design.objects.all()
    Codingdata=Coding.objects.all()
    Languagedata=Languages.objects.all()
    AllKnowledgedata=AllKnowledge.objects.all()    
    contactdetailsdata=contactdetails.objects.all()    
    personalinfodata=personalinfo.objects.all()
    personal_linksdata=personal_links.objects.all()
    
    
    if request.method == "GET":
        search=request.GET.get("search")
        
        if search != None:
             # Perform filtering based on category and location
            Bannerdata = property.objects.filter(Property_search__icontains=Banner)
            Socialmedia_Postdata = property.objects.filter(Property_search__icontains=search)
            Manipulationdata = property.objects.filter(Property_search__icontains=search)
            Web_Developmentdata = property.objects.filter(Property_search__icontains=search)
            return render(request, "searchresult.html", {'Bannerdata': Bannerdata})
    
    context={
        'form1':form1,
        'Bannerdata':Bannerdata,
        'Socialmedia_Postdata':Socialmedia_Postdata,
        'Manipulationdata':Manipulationdata,
        'Web_Developmentdata':Web_Developmentdata,
        'recentpost':recentpost,
        'recentwebsite':recentwebsite,
        'biodata':biodata,
        'infodata':infodata,
        'servicedata':servicedata,
        'pricedata':pricedata,
        'resumedata':resumedata,
        'Designdata':Designdata,
        'Codingdata':Codingdata,
        'Languagedata':Languagedata,
        'AllKnowledgedata':AllKnowledgedata,
        'contactdetailsdata':contactdetailsdata,
        'personalinfodata':personalinfodata,
        'personal_linksdata':personal_linksdata,
        
    }
    return render(request,"index.html",context)
   
def contactform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Basic form validation (add more as needed)
        if name and email and message:
            # Save data to the database
            contact_message = Contactform(name=name, email=email, message=message)
            contact_message.save()
            
            # Sending email to staff
            subject = "New Contact Enquiry"
            email_content = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            from_email = "chhonkarchirag886@gmail.com"
            recipient_list = ["chhonkarchirag886@gmail.com"]
            
            try:
                send_mail(subject, email_content, from_email, recipient_list,)
            except Exception as e:
                # Handle email sending failure (log, inform admin, etc.)
                print(f"Failed to send email: {e}")
        
        return render(request, "contactthank.html")
    
    return render(request, "contactthank.html")

    

def errorpage(request):
    personal_linksdata=personal_links.objects.all()
    
    context={
        "personal_linksdata":personal_linksdata
    }
    return render(request,"404.html",context)

def contactthank(request):
    return render(request,'contactthank.html')

def errormessage(request):
    personal_linksdata=personal_links.objects.all()
    
    context={
        "personal_linksdata":personal_linksdata
    }
    return render(request,"messageerror.html",context)

def download_cv(request):
    # Get the full path to the CV file
    cv_file_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'Chirag Chhonkar_WebDeveloper_CV.pdf')

    # Check if the file exists
    if os.path.exists(cv_file_path):
        # Open the file
        file = open(cv_file_path, 'rb')

        # Create a FileResponse object
        response = FileResponse(file)

        # Set the content type
        response['Content-Type'] = 'application/pdf'

        # Set the Content-Disposition
        response['Content-Disposition'] = 'attachment; filename="Chirag Chhonkar_WebDeveloper_CV.pdf"'

        # Set cache control headers
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'

        return response
    else:
        # Handle the case when the file doesn't exist
        return render(request,"404.html",)
