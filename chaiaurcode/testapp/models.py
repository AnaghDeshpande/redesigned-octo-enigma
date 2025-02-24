from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_VARIETIES = [
        ('ML','Masala'),
        ('GG','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELAICHI'),
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="chais/")
    date = models.DateField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_VARIETIES, default='ML')
    description = models.TextField(default=" ")

    def __str__(self):
        return self.name        #it will make changes in the admin site how to object is named- changed name from CHAIVARIETY OBJECT(1) TO name given
