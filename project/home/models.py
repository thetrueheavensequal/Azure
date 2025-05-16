from django.db import models
from django.contrib.auth.models import User


class EventType(models.Model):
    e_name = models.CharField(max_length=100)
    e_desc = models.TextField()
    e_pic = models.ImageField(upload_to='uploads/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.e_name

    class Meta:
        verbose_name_plural = 'Event-Types'



class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=100)
    c_phone = models.CharField(max_length=10)
    c_email = models.EmailField()
    e_name = models.ForeignKey(EventType, on_delete=models.CASCADE)
    appmnt_date = models.DateField()
    appmnt_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.e_name.e_name} ({self.appmnt_date})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
