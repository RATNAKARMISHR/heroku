# Generated by Django 3.0.10 on 2020-12-25 15:28

from django.db import migrations, models
import proApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.CharField(default=proApp.models.increment_role_id, max_length=25, verbose_name='UserID')),
                ('Firstname', models.CharField(default='', max_length=20)),
                ('Middlename', models.CharField(blank=True, default='', max_length=20)),
                ('Lastname', models.CharField(default='', max_length=255)),
                ('Username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('ifLogged', models.BooleanField(default=False)),
                ('role', models.CharField(default='', max_length=10)),
                ('mobile_No', models.CharField(default='', max_length=10)),
                ('Gender', models.CharField(default='', max_length=2)),
                ('City', models.CharField(default='', max_length=10)),
                ('State', models.CharField(default='', max_length=20)),
                ('zipcode', models.CharField(default='', max_length=6)),
            ],
        ),
    ]
