from django.db import models
from mainapp.managers.news_manager import NewsManager


class News(models.Model):
    objects = NewsManager()

    title = models.CharField(max_length=256, verbose_name='Title')
    preamble = models.CharField(max_length=1024, blank=True, null=True, verbose_name="Preamble")
    body = models.TextField(blank=False, null=False, verbose_name='Body')
    body_as_markdown = models.BooleanField(
        default=False,
        verbose_name="As markdown"
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of creating",
        editable=False
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Date of editing",
        editable=False
    )
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args):
        self.deleted = True
        self.save()


# class SubNews(models.Model):
#     body = models.TextField(blank=True, null=True)
#     news = models.ForeignKey(News, on_delete=models.CASCADE)
    # news = models.ManyToManyField(News, on_delete=models.CASCADE)

# python manage.py makemigrations
# python manage.py migrate


# python manage.py dbshell
# from mainapp.models import News

# python manage.py dumpdata mainapp.News > mainapp/fixture/0001_news.json
# pip install django-markdownify
# python manage.py loaddata 001_news

news = News.objects.create(title="Новость", body="Стандартная новость")
# print(news)
news.save()
news = News.objects.create(title="Новость2", body="Стандартная новость 2")
# print(news)
news.save()
news = News.objects.create(title="Новость3", body="Стандартная новость 3")
# print(news)
news.save()
news = News.objects.create(title="Новость4", body="Стандартная новость 4")
# print(news)
news.save()
news = News.objects.create(title="Новость5", body="Стандартная новость 5")
# print(news)
news.save()
news = News.objects.create(title="Новость6", body="Стандартная новость 6")
# print(news)
news.save()