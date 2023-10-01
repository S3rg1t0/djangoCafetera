from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                subject="La Caffettiera: Nuevo mensaje de contacto",
                body=f"De {name} <{email}>\n\n{content}",
                from_email="no-contestar@inbox.mailtrop.io",
                to=["sergioalonso@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse("contact") + "?ok")
            except:
                return redirect(reverse("contact")+"?fail")

    return render(request=request,
                  template_name="contact/contact.html",
                  context={"form": contact_form})
