# Generated by Django 4.1 on 2022-08-03 15:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0003_postovi_naslov_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='postovi',
            name='datum',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]