from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)

class Feedback(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    