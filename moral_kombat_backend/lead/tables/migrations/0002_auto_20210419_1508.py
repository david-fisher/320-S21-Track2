# Generated by Django 2.2.12 on 2021-04-19 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACTION_PAGE',
            fields=[
                ('CHOICE', models.TextField(default='default')),
                ('RESULT_PAGE', models.IntegerField(null=True)),
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('PAGE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_page1', to='tables.PAGES')),
                ('VERSION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_page2', to='tables.PAGES', to_field='VERSION', unique=True)),
            ],
            options={
                'unique_together': {('PAGE', 'CHOICE', 'ID', 'RESULT_PAGE')},
            },
        ),
        migrations.RemoveField(
            model_name='scenarios',
            name='PROFESSOR',
        ),
        migrations.CreateModel(
            name='RESPONSE_TO_ACTION_PAGE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACTION_PAGE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_page3', to='tables.ACTION_PAGE')),
                ('ACTION_PAGE_VERSION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_page4', to='tables.ACTION_PAGE', to_field='VERSION')),
                ('RESPONSE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_page2', to='tables.RESPONSES')),
            ],
        ),
    ]