# Generated by Django 3.1.1 on 2020-11-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='COURSE',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
