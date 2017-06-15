# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 08:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170613_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicAffairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bursar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.College')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='')),
                ('phone', models.CharField(default='', max_length=15)),
                ('rank', models.CharField(choices=[('1', 'Professor'), ('2', 'Associate Professor'), ('3', 'Senior Lecturer'), ('4', 'Lecturer I'), ('5', 'Lecturer II'), ('6', 'Assistant Lecturer'), ('7', 'Graduate Assistant')], default='', max_length=2)),
                ('status', models.CharField(choices=[('1', 'Permanent'), ('2', 'Adjunct')], default='', max_length=2)),
                ('dept', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAffairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(choices=[('1', 'Head'), ('2', 'Officer')], default=2, max_length=2)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='', max_length=5),
        ),
        migrations.AddField(
            model_name='student',
            name='genotype',
            field=models.CharField(choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('CS', 'CS')], default='', max_length=5),
        ),
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.FileField(default='', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Level'),
        ),
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Major'),
        ),
        migrations.AddField(
            model_name='student',
            name='modeOfEntry',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.ModeOfEntry'),
        ),
        migrations.AddField(
            model_name='student',
            name='oLevel',
            field=models.CharField(choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('WAEC/GCE', 'WAEC/GCE'), ('NECO/GCE', 'NECO/GCE'), ('WAEC/NECO', 'WAEC/NECO')], default='', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='parentNo',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('1', 'Normal'), ('2', 'Exchange'), ('3', 'Leave'), ('4', 'Sick'), ('5', 'Suspension'), ('6', 'Withdrawn')], default=1, max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='town',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='studentaffairs',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collegeofficer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bursar',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='academicaffairs',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]