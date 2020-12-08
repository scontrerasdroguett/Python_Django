from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    #print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            lastname = request.POST.get('lastname','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')

            #Correo que se enviará
            email= EmailMessage(
                "Adopta.me. nuevo mensaje",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["sca.contreras@alumnos.duoc.cl"],
                reply_to = [email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + "?OK")
            except:
                return redirect(reverse('contact') + "?FAIL")
            
    return render(request, "contact/contact.html", {'form':contact_form})