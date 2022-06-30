from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Blog(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey('Blogger', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})


class Blogger(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('blogger-detail', kwargs={'pk': self.pk})

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Blogger.objects.create(user=instance)
        instance.blogger.save()


class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    author = models.ForeignKey('Blogger', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=200)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.content
