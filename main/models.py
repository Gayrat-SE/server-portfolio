from django.db import models

# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'



class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    cv = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'




class IndexImage(models.Model):
    image = models.ImageField(upload_to='images/homepage/')
    
    class Meta:
        verbose_name = 'Index Image'
        verbose_name_plural = 'Index Images'