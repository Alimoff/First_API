from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField("Category", max_length=200)

    # More info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Videos(models.Model):
    name = models.CharField("Video", max_length=200)
    text = models.TextField("Description:")

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="videos"
    )

    # More info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "More Videos"
