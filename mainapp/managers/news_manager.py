from django.db import models
# from ..models import News


class NewsManager(models.Manager):
    def get_queryset(self):
        # return News.objects.filter(deleted=False)
        return super().get_queryset().filter(deleted=False)

