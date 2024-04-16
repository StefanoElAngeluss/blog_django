# from django.shortcuts import redirect, render, get_object_or_404
# from django.urls import reverse
# from store.models import Commande, Panier, Produit


# def store(request):
#     produits = Produit.objects.all()
#     return render(request, 'store/index.html',
#                   context={'produits': produits})


# def produit_detail(request, slug):
#     produit = get_object_or_404(Produit, slug=slug)
#     return render(request, 'store/detail.html',
#                   context={'produit': produit})


# def ajouter_au_panier(request, slug):
#     utilisateur = request.user
#     produit = get_object_or_404(Produit, slug=slug)
#     panier, _ = Panier.objects.get_or_create(utilisateur=utilisateur)
#     commande, created = Commande.objects.get_or_create(utilisateur=utilisateur,
#                                                        client=False,
#                                                        produit=produit)
#     if created:
#         panier.commandes.add(commande)
#         panier.save()
#     else:
#         commande.quantite += 1
#         commande.save()

#     return redirect(reverse("produit", kwargs={"slug": slug}))

# def panier(request):
#     panier = get_object_or_404(Panier, utilisateur=request.user)
#     return render(request, 'store/panier.html', context={"commandes": panier.commandes.all()})

# def delete_panier(request):
#     if panier := request.user.panier:
#         panier.delete()

#     return redirect('store')
