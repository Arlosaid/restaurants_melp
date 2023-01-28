from django.db import models

# Create your models here.
class Restaurants(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    rating = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        managed = False
        db_table = 'restaurants'
    
        def __str__(self):
            return f"{self.id}-{self.name}-{self.rating}-{self.site}-{self.email}-{self.phone}-{self.state}-{self.city}{self.street}-{self.lat}-{self.lng}"    