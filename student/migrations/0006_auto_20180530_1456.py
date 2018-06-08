# Generated by Django 2.0.4 on 2018-05-30 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20180530_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attendance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Attendance'),
        ),
        migrations.AlterField(
            model_name='student',
            name='fee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Fees'),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Guardian'),
        ),
        migrations.AlterField(
            model_name='student',
            name='progress',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Progress'),
        ),
        migrations.AlterField(
            model_name='student',
            name='rank',
            field=models.OneToOneField(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Rank'),
        ),
    ]