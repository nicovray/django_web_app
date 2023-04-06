from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 
            'listings/band_list.html',
            {'bands': bands})

def band_detail(request, band_id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=band_id)
    return render(request,
            'listings/band_detail.html',
            {'band': band}) # nous passons l'id au modèle

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # Mise à jour du groupe existant dans la base de données
            form.save()
            # Redirection vers la page de détail correspondant au groupe que nous venons de mettre à jour
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm(instance=band)

    return render(request,
                  'listings/band_update.html',
                  {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 
            'listings/listing_list.html',
            {'listings': listings})

def listing_detail(request, listing_id):  # notez le paramètre id supplémentaire
    listing = Listing.objects.get(id=listing_id)
    return render(request,
            'listings/listing_detail.html',
            {'listing': listing}) # nous passons l'id au modèle

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Annonce » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})

def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # Mise à jour du groupe existant dans la base de données
            form.save()
            # Redirection vers la page de détail correspondant au groupe que nous venons de mettre à jour
            return HttpResponseRedirect(reverse('listing-detail', kwargs={'id': listing.id}))
    else:
        form = ListingForm(instance=listing)

    return render(request,
                  'listings/listing_update.html',
                  {'form': form})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        listing.delete()
        # rediriger vers la liste des groupes
        return redirect('listing-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/listing_delete.html',
                    {'listing': listing})

def about(request):
    return render(request, 
            'listings/about.html')

def contact(request):
    if request.method == 'POST':
        # Création d'une instance de notre formulaire et remplissage de ce dernier avec les données du POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('/bands')
        # Si le formulaire n'est pas valide, nous devons continuons le programme en éxécutons le return

    else:
        # Ceci devrait être une requête GET, du coup nous créons un formulaire vide
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')