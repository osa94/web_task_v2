# Generated by Django 2.2.1 on 2019-05-14 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exams', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=500)),
                ('max_points', models.FloatField()),
                ('exam', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='exams.Exam')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='teachers.Teacher')),
            ],
        ),
    ]
