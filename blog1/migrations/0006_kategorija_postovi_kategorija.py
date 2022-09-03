# Generated by Django 4.1 on 2022-08-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0005_alter_postovi_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='postovi',
            name='kategorija',
            field=models.CharField(default='ostalo', max_length=255),
        ),
    ]