from django.http import HttpResponse
from listings.models import Band, Listing
from django.shortcuts import render
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    # Set template page to use in response
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})

def band_detail(request, band_id):                  # band_id is defined in urls.py, as url address
    band = Band.objects.get(id=band_id)             # Get object from db with id = band_id
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})                   # Object band as set previously is named band

def about(request):
    return render(request,'structure/about.html')
#    return HttpResponse('<h1>A propos</h1> <p>Découvrez l\'ensemble de nos équipes!</p>')

# def contact(request):
#     return render (request, 'structure/contact.html')

def contact(request):
    # print('La méthode de requête est : ', request.method)
    # print ('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        # create a form instance and fill it in with POST data
        form = ContactUsForm(request.POST)

        # if form is valid, send an email to admin@mercherx.fr
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.fr']
            )
            return redirect('email-sent')

    else:
        # create and empty form
        form = ContactUsForm()

    return render(request,
                  'structure/contact.html',
                  {'form': form}
        )



def listings(request):
    lists = Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'lists': lists}
                  )