from django.db import models


class Button(models.Model):
    light_on = models.BooleanField(default=False)
    def __str__(self):
        return "The light is ON" if self.light_on else "The light is OFF"


    def save(self, *args, **kwargs):
        self.pk = 1
        super(Button, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
