# Generated by Django 5.0.2 on 2024-02-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField(unique=True)),
                ('f_name', models.CharField(max_length=60)),
                ('l_name', models.CharField(max_length=60)),
                ('product', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
