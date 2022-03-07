from django.db import models
from django.contrib.auth.models import User

from datetime import date

audit_zone_choices = (
    ("Фабрика", "Фабрика"), ("Склад", "Склад"), ("Улица", "Улица"),
)
type_of_risk_choices = (
    ("Падение", "Падение"), ("Удар", "Удар"), ("Контузия", "Контузия"),
)
level_of_risk_choices = (
    ("Низкий", "Низкий"), ("Средний", "Средний"), ("Высокий", "Высокий"),
)


class Audit(models.Model):
    performer = models.ForeignKey(User, verbose_name='Исполнитель', on_delete=models.CASCADE)
    date_added = models.DateField(default=date.today)
    audit_zone = models.CharField('Зона аудита', choices=audit_zone_choices, max_length=200)
    type_of_risk = models.CharField('Оцениваемый риск', choices=type_of_risk_choices, max_length=200)
    level_of_risk = models.CharField('Уровень риска', choices=level_of_risk_choices, max_length=200)

    class Meta:
        verbose_name = 'Аудит'
        verbose_name_plural = 'Аудиты'
