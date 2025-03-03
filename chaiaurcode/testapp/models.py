from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

# ONE - TO - MANY RELATION
class chaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TimeField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    

# MANY-TO-MANY RELATION
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name    
    
# ONE - TO - MANY   
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=10)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.name}'    