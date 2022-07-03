from django.db import models

# Create your models here.


class Videos(models.Model):
    name = models.CharField("Video", max_length=200)
    text = models.TextField("Description:")

    # More info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "More Videos"
