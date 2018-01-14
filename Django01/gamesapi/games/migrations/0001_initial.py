# Generated by Django 2.0.1 on 2018-01-03 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('release_date', models.DateTimeField()),
                ('game_category', models.CharField(blank=True, default='', max_length=200)),
                ('played', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),

        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=False, default='Anonymoose', max_length=200)),
                ('age', models.CharField(blank=False, default='100', max_length=200)),

            ],
            options={

            },


        ),
    ]
