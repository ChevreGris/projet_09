from imp import IMP_HOOK
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from litreview_app.models import Ticket, Review
from authentication_app.forms import TicketForm, TicketReviewFrom


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def ticket_list(request):
   tickets = Ticket.objects.filter(user=request.user)
   return render(request,
           'litreview_app/ticket_list.html',
           {'tickets': tickets})

@login_required
def ticket_list(request):
   tickets = Ticket.objects.all()
   return render(request,
           'litreview_app/ticket_list.html',
           {'tickets': tickets})

@login_required
def ticket_detail(request, id):
  ticket = Ticket.objects.get(id=id)
  return render(request,
          'litreview_app/ticket_detail.html',
          {'ticket': ticket})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            # créer un nouvel « ticket » et la sauvegarder dans la db
            ticket = form.save()
            # redirige vers la page de détail du ticket que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('ticket_detail', ticket.id)
        #import pdb; pdb.set_trace()
    else:
        form = TicketForm()

    return render(request,
            'litreview_app/ticket_create.html',
            {'form': form})

@login_required
def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('ticket_detail', ticket.id)
    else:
        form = TicketForm(instance=ticket)

    return render(request,
                'litreview_app/ticket_update.html',
                {'form': form})

@login_required
def ticket_delete(request, id):
    ticket = Ticket.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        ticket.delete()
        # rediriger vers la liste des groupes
        return redirect('ticket_list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'litreview_app/ticket_delete.html',
                    {'ticket': ticket})

@login_required
def review_create(request):
    if request.method == 'POST':
        form = TicketReviewFrom(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            # créer un nouvel « ticket » et la sauvegarder dans la db
            review = form.save()
            # redirige vers la page de détail du ticket que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('ticket_detail', review.id)
        #import pdb; pdb.set_trace()
    else:
        form = TicketReviewFrom()

    return render(request,
            'litreview_app/review_create.html',
            {'form': form})

@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request,
           'litreview_app/review_list.html',
           {'reviews': reviews})

@login_required
def review_detail(request, id):
    review = Review.objects.get(id=id)
    ticket = Ticket.objects.get(id=id)
    return render(request,
          'litreview_app/review_detail.html',
          {'review': review})
