from django.db import models


# Create your models here.
class top_vacancies_skillls(models.Model):
    name = models.TextField()
    count = models.IntegerField()
    year = models.IntegerField(default="0")

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"name: {self.name},count: {self.count}, year: {self.year}"


class geography_model(models.Model):
    name = models.CharField(max_length=200)
    aver_salary = models.IntegerField()
    share = models.FloatField()

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"name: {self.name},aver_salary: {self.aver_salary}, share: {self.share}"


class demand_model(models.Model):
    name = models.CharField(max_length=200)
    aver_salary = models.IntegerField()
    count = models.IntegerField()
    year = models.IntegerField(default="0")