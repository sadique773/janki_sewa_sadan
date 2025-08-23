from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    specialization = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return f"{self.name} ({self.specialization})"
    


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return f"Photo {self.id}"