from django.db import models


CATEGORY = (
    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)

LANGUAGE  = (
    ('EN', 'ENGLISH'),
    ('BN', 'BANGLA'),
)

STATUS = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)

class Movie(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length = 1000)
    image = models.ImageField(upload_to = 'movies')
    
    category = models.CharField(choices = CATEGORY, max_length = 100)
    language = models.CharField(choices = LANGUAGE, max_length = 100)
    status = models.CharField(choices = STATUS, max_length = 100)
    
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title
    
