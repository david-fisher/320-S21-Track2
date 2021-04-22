# Generated by Django 3.1.7 on 2021-04-22 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_auto_20210421_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professors_to_scenario',
            name='PROFESSOR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professors_to_scenario1', to='tables.professors', unique=True),
        ),
        migrations.AddField(
            model_name='professors_to_scenario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]