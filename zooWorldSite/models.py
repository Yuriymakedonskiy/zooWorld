from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
    
class Rating(models.Model):
    name = models.CharField(max_length=254,verbose_name="Имя",default=None)
    review = models.CharField(max_length=254, verbose_name="Отзыв",default=None)
    score = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ],
    )

    def __str__(self):
        return str(self.name)
