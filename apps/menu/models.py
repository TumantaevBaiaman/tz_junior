from django.db import models
from django.utils import timezone


class Menu(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"


class SubMenu(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.menu_id_id}{self.name}"

    class Meta:
        verbose_name = "Sub Menu"
        verbose_name_plural = "Sub Menu"


class Rating(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.name}{self.rating}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Rating"


