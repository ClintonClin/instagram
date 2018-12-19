from django.db import models
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    
    profile_image = ImageField(null=True, blank=True)
    profile_bio = HTMLField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['user']

    def save_profile(self):
        self.save()

    @classmethod
    def profile_search(cls, tag):
        profile = Profile.objects.filter(user__username__icontains=tag)
        return profile

    @classmethod
    def acquire_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile


class Image(models.Model):
    
    photo = ImageField(null=True, blank=True)
    image_name = models.CharField(max_length=50)
    image_caption = HTMLField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.photo)

    class Meta:
        ordering = ['-date_posted']

    def save_image(self):
        self.save()

    @classmethod
    def acquire_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image

    @classmethod
    def acquire_profile_image(cls, profile):
        images = Image.objects.filter(profile__pk=profile)
        return images

    @classmethod
    def acquire_all_images(cls):
        images = Image.objects.all()
        return images


class Comment(models.Model):

    comment = HTMLField(null=True, blank=True)
    post_date = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    @classmethod
    def acquire_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments
