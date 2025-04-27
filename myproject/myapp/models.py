from django.db import models

# myapp/models.py
# models.py
class Service(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='services/')
    slug = models.SlugField(unique=True)
    description = models.TextField()
    extra_info = models.TextField(blank=True, null=True)
    bullets = models.TextField(help_text="Separate each item with a semicolon (;)")
    brochure_1 = models.FileField(upload_to='brochures/', blank=True, null=True)
    brochure_2 = models.FileField(upload_to='brochures/', blank=True, null=True)
    is_active = models.BooleanField(default=True)  # ✅ Add this line

    def get_bullet_list(self):
        return [b.strip() for b in self.bullets.split(';') if b.strip()]

    def __str__(self):
        return self.title


from django.db import models
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, default="Admin")
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

