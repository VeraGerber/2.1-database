

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
