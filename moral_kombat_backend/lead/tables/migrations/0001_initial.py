# Generated by Django 2.2.12 on 2021-05-06 16:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('course', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField()),
                ('page_type', models.CharField(choices=[('I', 'INTRO'), ('F', 'FEEDBACK'), ('G', 'GENERIC'), ('R', 'REFLECTION'), ('S', 'STAKEHOLDER'), ('A', 'ACTION')], max_length=2)),
                ('page_title', models.CharField(max_length=1000)),
                ('version', models.IntegerField(default=1)),
                ('body', models.TextField(blank=True, null=True)),
                ('x_coordinate', models.IntegerField()),
                ('y_coordinate', models.IntegerField()),
                ('completed', models.BooleanField(default=False)),
                ('next_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages2', to='tables.pages')),
            ],
            options={
                'db_table': 'pages',
            },
        ),
        migrations.CreateModel(
            name='professors',
            fields=[
                ('professor', models.TextField(primary_key=True, serialize=False)),
                ('fname', models.TextField()),
                ('lname', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'professors',
            },
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('question', models.IntegerField()),
                ('version', models.IntegerField()),
                ('points', models.IntegerField()),
                ('question_text', models.TextField(blank=True)),
                ('question_summary', models.TextField(blank=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'questions',
                'unique_together': {('question', 'version')},
            },
        ),
        migrations.CreateModel(
            name='responses',
            fields=[
                ('response_id', models.AutoField(primary_key=True, serialize=False)),
                ('response', models.IntegerField()),
                ('version', models.IntegerField()),
                ('date_taken', models.DateField(auto_now_add=True)),
                ('choice', models.TextField()),
                ('course', models.ForeignKey(db_column='course', on_delete=django.db.models.deletion.CASCADE, to='tables.courses')),
                ('page', models.ForeignKey(db_column='page', on_delete=django.db.models.deletion.CASCADE, to='tables.pages')),
            ],
            options={
                'db_table': 'responses',
            },
        ),
        migrations.CreateModel(
            name='scenarios',
            fields=[
                ('scenario_id', models.AutoField(primary_key=True, serialize=False)),
                ('scenario', models.IntegerField(default=1)),
                ('version', models.IntegerField(default=1)),
                ('name', models.TextField(max_length=50)),
                ('public', models.BooleanField(default=False)),
                ('num_conversation', models.IntegerField(default=0)),
                ('is_finished', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'scenarios',
                'unique_together': {('scenario', 'version')},
            },
        ),
        migrations.CreateModel(
            name='stakeholders',
            fields=[
                ('stakeholder', models.IntegerField()),
                ('version', models.IntegerField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('job', models.TextField()),
                ('introduction', models.TextField()),
                ('enable_multi_convo', models.BooleanField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('scenario', models.ForeignKey(db_column='scenario', on_delete=django.db.models.deletion.CASCADE, to='tables.scenarios')),
            ],
            options={
                'db_table': 'stakeholders',
                'unique_together': {('stakeholder', 'version')},
            },
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('student', models.TextField(primary_key=True, serialize=False)),
                ('fname', models.TextField()),
                ('lname', models.TextField()),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='reflections_taken',
            fields=[
                ('reflections', models.TextField(blank=True)),
                ('response_id', models.OneToOneField(db_column='response_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tables.responses')),
            ],
            options={
                'db_table': 'reflections_taken',
            },
        ),
        migrations.CreateModel(
            name='students_to_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(db_column='course', on_delete=django.db.models.deletion.CASCADE, to='tables.courses')),
                ('student', models.ForeignKey(db_column='student', on_delete=django.db.models.deletion.CASCADE, to='tables.students')),
            ],
            options={
                'db_table': 'students_to_course',
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='scenarios_for',
            fields=[
                ('version', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(db_column='course', on_delete=django.db.models.deletion.CASCADE, to='tables.courses')),
                ('scenario_id', models.ForeignKey(db_column='scenario_id', on_delete=django.db.models.deletion.CASCADE, to='tables.scenarios')),
            ],
            options={
                'db_table': 'scenarios_for',
                'unique_together': {('scenario_id', 'course')},
            },
        ),
        migrations.AddField(
            model_name='responses',
            name='scenario',
            field=models.ForeignKey(db_column='scenario', on_delete=django.db.models.deletion.CASCADE, to='tables.scenarios'),
        ),
        migrations.AddField(
            model_name='responses',
            name='student',
            field=models.ForeignKey(db_column='student', on_delete=django.db.models.deletion.CASCADE, to='tables.students'),
        ),
        migrations.CreateModel(
            name='reflection_questions',
            fields=[
                ('reflection_question_id', models.IntegerField()),
                ('reflection_question', models.TextField()),
                ('version', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'reflection_questions',
                'unique_together': {('reflection_question_id', 'version')},
            },
        ),
        migrations.CreateModel(
            name='professors_to_courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(db_column='course', on_delete=django.db.models.deletion.CASCADE, to='tables.courses')),
                ('professor', models.ForeignKey(db_column='professor', on_delete=django.db.models.deletion.CASCADE, to='tables.professors')),
            ],
            options={
                'db_table': 'professors_to_courses',
                'unique_together': {('professor', 'course')},
            },
        ),
        migrations.AddField(
            model_name='pages',
            name='scenario',
            field=models.ForeignKey(db_column='scenario', on_delete=django.db.models.deletion.CASCADE, related_name='pages1', to='tables.scenarios'),
        ),
        migrations.CreateModel(
            name='issues',
            fields=[
                ('issue', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('importance_score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('scenario_id', models.ForeignKey(db_column='scenario_id', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='issues1', to='tables.scenarios')),
            ],
            options={
                'db_table': 'issues',
            },
        ),
        migrations.CreateModel(
            name='demographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.SmallIntegerField()),
                ('grade', models.CharField(choices=[('0', 'Other'), ('1', 'Freshmen'), ('2', 'Sophomore'), ('3', 'Junior'), ('4', 'Senior')], max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OT', 'Other')], max_length=2)),
                ('race', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30)),
                ('student', models.ForeignKey(db_column='student', on_delete=django.db.models.deletion.CASCADE, related_name='demographics', to='tables.students', unique=True)),
            ],
            options={
                'db_table': 'demographics',
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='professors',
            field=models.ManyToManyField(related_name='courses', through='tables.professors_to_courses', to='tables.professors'),
        ),
        migrations.AddField(
            model_name='courses',
            name='scenarios',
            field=models.ManyToManyField(related_name='courses', through='tables.scenarios_for', to='tables.scenarios'),
        ),
        migrations.AddField(
            model_name='courses',
            name='students',
            field=models.ManyToManyField(related_name='courses', through='tables.students_to_course', to='tables.students'),
        ),
        migrations.CreateModel(
            name='conversations',
            fields=[
                ('conversation', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('response', models.TextField()),
                ('question_summary', models.TextField()),
                ('stakeholder', models.ForeignKey(db_column='stakeholder', on_delete=django.db.models.deletion.CASCADE, related_name='conversations1', to='tables.stakeholders')),
            ],
            options={
                'db_table': 'conversations',
            },
        ),
        migrations.CreateModel(
            name='action_page',
            fields=[
                ('action_page_id', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('version', models.IntegerField()),
                ('choice', models.TextField()),
                ('result_page', models.IntegerField()),
                ('page', models.ForeignKey(db_column='page', on_delete=django.db.models.deletion.CASCADE, related_name='action_page1', to='tables.pages')),
            ],
            options={
                'db_table': 'action_page',
                'unique_together': {('action_page_id', 'version')},
            },
        ),
        migrations.CreateModel(
            name='student_times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateField(auto_now=True)),
                ('page', models.IntegerField()),
                ('start_time', models.DateField(auto_now_add=True)),
                ('end_time', models.DateField(blank=True, null=True)),
                ('course', models.ForeignKey(db_column='course', on_delete=django.db.models.deletion.CASCADE, to='tables.courses')),
                ('scenario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.scenarios')),
                ('student', models.ForeignKey(db_column='student', on_delete=django.db.models.deletion.CASCADE, to='tables.students')),
            ],
            options={
                'db_table': 'student_times',
                'unique_together': {('student', 'course', 'scenario_id')},
            },
        ),
        migrations.CreateModel(
            name='stakeholders_to_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(db_column='question', on_delete=django.db.models.deletion.CASCADE, to='tables.questions')),
                ('stakeholder', models.ForeignKey(db_column='stakeholder', on_delete=django.db.models.deletion.CASCADE, to='tables.stakeholders')),
            ],
            options={
                'db_table': 'stakeholders_to_questions',
                'unique_together': {('stakeholder', 'question')},
            },
        ),
        migrations.CreateModel(
            name='stakeholder_to_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(db_column='page', on_delete=django.db.models.deletion.CASCADE, to='tables.pages')),
                ('stakeholder', models.ForeignKey(db_column='stakeholder', on_delete=django.db.models.deletion.CASCADE, to='tables.stakeholders')),
            ],
            options={
                'db_table': 'stakeholder_to_page',
                'unique_together': {('page', 'stakeholder')},
            },
        ),
        migrations.CreateModel(
            name='responses_to_conversations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stakeholder_version', models.IntegerField()),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('conversation', models.ForeignKey(db_column='conversation', on_delete=django.db.models.deletion.CASCADE, to='tables.conversations')),
                ('response_id', models.ForeignKey(db_column='response_id', on_delete=django.db.models.deletion.CASCADE, to='tables.responses')),
                ('stakeholder', models.ForeignKey(db_column='stakeholder', on_delete=django.db.models.deletion.CASCADE, to='tables.stakeholders')),
            ],
            options={
                'db_table': 'responses_to_conversations',
                'unique_together': {('response_id', 'conversation')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='responses',
            unique_together={('response', 'student', 'scenario', 'page', 'course', 'date_taken')},
        ),
        migrations.CreateModel(
            name='response_to_action_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_page', models.ForeignKey(db_column='action_page', on_delete=django.db.models.deletion.CASCADE, to='tables.action_page')),
                ('response_id', models.ForeignKey(db_column='response', on_delete=django.db.models.deletion.CASCADE, to='tables.responses')),
            ],
            options={
                'db_table': 'response_to_action_page',
                'unique_together': {('response_id', 'action_page')},
            },
        ),
        migrations.CreateModel(
            name='reflection_question_to_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.ForeignKey(db_column='page', on_delete=django.db.models.deletion.CASCADE, related_name='reflection_questions_to_page1', to='tables.pages')),
                ('reflection_question_id', models.ForeignKey(db_column='reflection_question_id', on_delete=django.db.models.deletion.CASCADE, to='tables.reflection_questions')),
            ],
            options={
                'db_table': 'reflection_question_to_page',
                'unique_together': {('reflection_question_id', 'page_id')},
            },
        ),
        migrations.CreateModel(
            name='professors_to_scenario',
            fields=[
                ('permission', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('professor', models.ForeignKey(db_column='professor', on_delete=django.db.models.deletion.CASCADE, related_name='pts1', to='tables.professors')),
                ('scenario', models.ForeignKey(db_column='scenario', on_delete=django.db.models.deletion.CASCADE, related_name='pts2', to='tables.scenarios')),
            ],
            options={
                'db_table': 'professors_to_scenario',
                'unique_together': {('professor', 'scenario')},
            },
        ),
        migrations.CreateModel(
            name='pages_to_scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.ForeignKey(db_column='page', on_delete=django.db.models.deletion.CASCADE, related_name='stakeholder_page1', to='tables.pages')),
                ('scenario_id', models.ForeignKey(db_column='scenario', on_delete=django.db.models.deletion.CASCADE, related_name='stakeholder_page2', to='tables.scenarios')),
            ],
            options={
                'db_table': 'pages_to_scenario',
                'unique_together': {('page_id', 'scenario_id')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='pages',
            unique_together={('page', 'version')},
        ),
        migrations.CreateModel(
            name='generic_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generic_page_id', models.IntegerField()),
                ('body', models.TextField()),
                ('version', models.IntegerField()),
                ('page', models.ForeignKey(db_column='page', on_delete=django.db.models.deletion.CASCADE, related_name='generic_page1', to='tables.pages')),
            ],
            options={
                'db_table': 'generic_page',
                'unique_together': {('generic_page_id', 'version')},
            },
        ),
        migrations.CreateModel(
            name='coverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverage_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('issue', models.ForeignKey(db_column='issue', on_delete=django.db.models.deletion.CASCADE, related_name='coverage1', to='tables.issues')),
                ('stakeholder', models.ForeignKey(db_column='stakeholder', on_delete=django.db.models.deletion.CASCADE, related_name='coverage2', to='tables.stakeholders')),
            ],
            options={
                'db_table': 'coverage',
                'unique_together': {('stakeholder', 'issue')},
            },
        ),
        migrations.CreateModel(
            name='courses_to_scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField()),
                ('course', models.ForeignKey(db_column='course', on_delete=django.db.models.deletion.CASCADE, to='tables.courses')),
                ('scenario', models.ForeignKey(db_column='scenario_id', on_delete=django.db.models.deletion.CASCADE, to='tables.scenarios')),
            ],
            options={
                'db_table': 'courses_to_scenario',
                'unique_together': {('course', 'scenario')},
            },
        ),
    ]
