# Generated by Django 5.0.6 on 2024-07-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_alter_activity_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
