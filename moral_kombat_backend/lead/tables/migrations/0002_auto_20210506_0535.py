# Generated by Django 3.1.7 on 2021-05-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenarios_for',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
