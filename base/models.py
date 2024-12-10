from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


# Create your models here.
class PublishState(models.Model):
    class State(models.IntegerChoices):
        DRAFT = 1, "پیش‌نویس"
        PUBLISHED = 2, "منتشر شده"
        ARCHIVED = 3 , "بایگانی شده"

    state = models.IntegerField(
        choices=State.choices,
        default=State.DRAFT
    )
    def __str__(self):
        return self.get_state_display()




class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    author = models.CharField(max_length=100 , validators=[MinLengthValidator(6)])
    slug = models.SlugField(unique=True,blank=True)
    state = models.ForeignKey(PublishState,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title} + {self.title[0]} + 'page' + {self.title[-1]}")
        super().save(*args, **kwargs) 

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.title}"
    
class UserComment(models.Model):
    post = models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return f"Comment by {self.username} on {self.post.title}"
    class Meta:
        ordering = ['-created_at'] 