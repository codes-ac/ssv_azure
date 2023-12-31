# Generated by Django 3.1.4 on 2020-12-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_atl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='showcase')),
                ('desc', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
