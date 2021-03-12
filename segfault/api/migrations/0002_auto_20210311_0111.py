# Generated by Django 3.1.7 on 2021-03-11 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scenario',
            options={'ordering': ['date_created', 'name']},
        ),
        migrations.AddField(
            model_name='course',
            name='fullName',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.CreateModel(
            name='partof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_scenarios', to='api.course')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='of_class', to='api.scenario')),
            ],
            options={
                'unique_together': {('scenario', 'course')},
            },
        ),
    ]
