# Generated by Django 4.2.7 on 2023-11-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_personifika_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personifika',
            name='first_name',
            field=models.CharField(max_length=252),
        ),
    ]
