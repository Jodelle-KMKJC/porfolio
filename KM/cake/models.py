from django.db import models

class Gateau(models.Model):
    CATEGORIE_CHOICES = (
        ('anniversaire', 'Anniversaire'),
        ('mariage', 'Mariage'),
        ('dessert', 'Dessert'),
        ('autre', 'Autre'),
    )

    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='gateaux/', blank=True, null=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    disponibilite = models.BooleanField(default=True)
    avis = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.nom