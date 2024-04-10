from django.contrib import admin
from store.models import Produit, Commande, Panier

class ProduitAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nom',)}

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Commande)
admin.site.register(Panier)
