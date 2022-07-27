# Generated by Django 2.1 on 2022-07-27 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('ApplicationId', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('ExperienceId', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=500)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('work_or_education', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('JobTitle', models.CharField(max_length=500)),
                ('JobId', models.AutoField(primary_key=True, serialize=False)),
                ('Location', models.CharField(max_length=500)),
                ('Experience_required', models.IntegerField()),
                ('Skills_required', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('OrganizationName', models.CharField(max_length=500)),
                ('OrganizationId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UsersInformation',
            fields=[
                ('UserName', models.CharField(max_length=500)),
                ('EmailAddress', models.CharField(max_length=500)),
                ('PhoneNumber', models.IntegerField()),
                ('password', models.CharField(max_length=500)),
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='EmployerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.UsersInformation'),
        ),
        migrations.AddField(
            model_name='job',
            name='OrganizationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.Organization'),
        ),
        migrations.AddField(
            model_name='experience',
            name='OrganizationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.Organization'),
        ),
        migrations.AddField(
            model_name='experience',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.UsersInformation'),
        ),
        migrations.AddField(
            model_name='application',
            name='ApplicantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.UsersInformation'),
        ),
        migrations.AddField(
            model_name='application',
            name='JobId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.Job'),
        ),
    ]
