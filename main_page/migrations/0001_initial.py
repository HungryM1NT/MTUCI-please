# Generated by Django 3.2.21 on 2023-10-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='persons_images')),
                ('surname', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('middle_name', models.CharField(max_length=128)),
            ],
        ),
    ]
