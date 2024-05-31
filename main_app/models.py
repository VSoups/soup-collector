from django.db import models
from django.urls import reverse

# Create your models here.

MEAL_RATINGS = [
    ('ON', 1),
    ('TW', 2),
    ('TH', 3),
    ('FO', 4),
    ('FI', 5),
]

class Soup(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    broth = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.id}'
    
    # must be named 'get_absolute_url'?
    def get_absolute_url(self):
        # 'reverse' allows the use of the url template from urls.py
        return reverse('detail', kwargs={'soup_id': self.id})
    
class Meal(models.Model):
    date = models.DateField('meal date')
    rating = models.CharField(
        max_length=2,
        choices=MEAL_RATINGS,
        default=MEAL_RATINGS[0][0],
    )

    soup = models.ForeignKey(Soup, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating: {self.get_rating_display()} on {self.date}"
    