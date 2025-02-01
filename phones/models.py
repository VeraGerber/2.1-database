from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    class Phone(models.Model):
        # TODO: Добавьте требуемые поля
        name = models.CharField(max_length=100)
        price = models.IntegerField(default=0)
        image = models.URLField(default='')
        release_date = models.DateField(default=1)
        lte_exists = models.BooleanField(default=False)
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Phone, self).save(*args, **kwargs)
    pass
