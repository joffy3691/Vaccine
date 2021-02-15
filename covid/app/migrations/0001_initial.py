# Generated by Django 3.1.6 on 2021-02-10 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('total_Vaccine', models.IntegerField()),
                ('available_Vaccine', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('hospital', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('fulfilled', models.BooleanField()),
                ('confirmtime', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('details_filled', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
                ('pneumonia', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('user', models.IntegerField(default='1')),
                ('obesity', models.BooleanField(default=False)),
                ('breathing', models.BooleanField(default=False)),
                ('pregnant', models.BooleanField(default=False)),
                ('smoker', models.BooleanField(default=False)),
                ('diabetic', models.BooleanField(default=False)),
                ('heart', models.BooleanField(default=False)),
                ('asthma', models.BooleanField(default=False)),
                ('blood', models.BooleanField(default=False)),
                ('others', models.BooleanField(default=False)),
            ],
        ),
    ]
