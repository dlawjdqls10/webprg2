# Generated by Django 2.1.7 on 2019-05-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(null=True)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
