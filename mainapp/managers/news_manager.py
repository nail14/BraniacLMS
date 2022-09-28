from django.db import models
# # from ..models import News


class NewsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

