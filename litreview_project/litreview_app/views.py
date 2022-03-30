from imp import IMP_HOOK
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from django.conf import settings
from itertools import chain
from django.db.models import CharField, Value
from django.shortcuts import render
from litreview_app.models import Ticket, Review, UserFollows
from authentication_app.forms import TicketForm, TicketReviewFrom, ReviewForTicketFrom, SubForm


@login_required
def home(request):
    return render(request, 'home.html')

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
        form = TicketForm(user=request.user)

    return render(request,
            'litreview_app/ticket_create.html',
            {'form': form})

@login_required
def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket, user=request.user)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('ticket_detail', ticket.id)
    else:
        form = TicketForm(instance=ticket, user=request.user)

    return render(request,
                'litreview_app/ticket_update.html',
                {'form': form})

@login_required
def ticket_add_review(request, id):
    ticket = Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = ReviewForTicketFrom(request.POST, request.FILES, user=request.user, ticket=ticket)
        if form.is_valid():
            # créer un nouvel « ticket » et la sauvegarder dans la db
            review = form.save()
            # redirige vers la page de détail du ticket que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('ticket_detail', review.id)
    else:
        form = ReviewForTicketFrom(user=request.user, ticket=ticket)

    return render(request,
            'litreview_app/ticket_review_create.html',
            {'form': form, 'ticket': ticket})

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
        form = TicketReviewFrom(user=request.user)

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
    return render(request,
          'litreview_app/review_detail.html',
          {'review': review, 'ticket': review.ticket})


@login_required
def sub(request):
    if request.method == 'POST':
        form = SubForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            UserFollows.objects.create(user=request.user, followed_user=form.cleaned_data['search'])
            return redirect('user_social')
    else:
        form = SubForm(user=request.user)

    followed_user = UserFollows.objects.filter(user=request.user)
    following_user = UserFollows.objects.filter(followed_user=request.user)
    
    return render(request,
            'litreview_app/user_social.html',
            {'form': form, 'followed_user': followed_user, 'following_user': following_user })
"""
@login_required
def flux(request):
    followed_user = UserFollows.objects.filter(user=request.user)
    bord_user = []
    for u in followed_user :
        bord_user.append(u.followed_user)
    user_reviews = Review.objects.filter(user=2)
    user_tickets = Ticket.objects.filter(user=2)
    user_reviews = user_reviews.annotate(content_type=Value('REVIEW', CharField()))
    user_tickets = user_tickets.annotate(content_type=Value('TICKET', CharField()))
    print(user_reviews)
    import pdb; pdb.set_trace()
    posts = sorted(
        chain(user_tickets, user_reviews), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    
    return render(request, 'litreview_app/flux.html', context={'posts': posts})
"""
@login_required
def flux(request):
    followed_user = UserFollows.objects.filter(user=request.user)
    bord_user = []
    a = []
    b = []
    c = []
    d = []
    for u in followed_user :
        bord_user.append(u.followed_user)
    for u in bord_user :
        user_reviews = Review.objects.filter(user=u)
        user_tickets = Ticket.objects.filter(user=u)
        user_reviews = user_reviews.annotate(content_type=Value('REVIEW', CharField()))
        user_tickets = user_tickets.annotate(content_type=Value('TICKET', CharField()))
        a.append(user_reviews)
        b.append(user_tickets)
    for i in a :
        for e in i:
            c.append(e)
    for i in b :
        for e in i :
            d.append(e)
    posts = sorted(
        chain(c, d), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    
    return render(request, 'litreview_app/flux.html', context={'posts': posts})

@login_required
def user_post(request):
    user_reviews = Review.objects.filter(user=request.user)
    user_reviews = user_reviews.annotate(content_type=Value('REVIEW', CharField()))
    user_tickets = Ticket.objects.filter(user=request.user)
    user_tickets = user_tickets.annotate(content_type=Value('TICKET', CharField()))
    posts = sorted(
        chain(user_reviews, user_tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    return render(request, 'litreview_app/user_post.html', context={'posts': posts})


#<QuerySet [<Review: Review object (3)>, <Review: Review object (4)>, <Review: Review object (5)>]>

#[<QuerySet [<Review: Review object (3)>, <Review: Review object (4)>, <Review: Review object (5)>]>, <QuerySet [<Review: Review object (10)>, <Review: Review object (11)>]>]

#[<QuerySet [<Review: Review object (3)>, <Review: Review object (4)>, <Review: Review object (5)>]>, <QuerySet [<Review: Review object (10)>, <Review: Review object (11)>]>]

#            [<Review: Review object (3)>, <Review: Review object (4)>, <Review: Review object (5)>, <Review: Review object (10)>, <Review: Review object (11)>]