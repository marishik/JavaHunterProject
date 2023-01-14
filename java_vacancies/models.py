from django.db import models

# Create your models here.
class top_vacancies_skillls(models.Model):
    name = models.TextField()
    count = models.IntegerField()
    year = models.IntegerField(default="0")

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"name: {self.name},count: {self.count}, year: {self.year}"

