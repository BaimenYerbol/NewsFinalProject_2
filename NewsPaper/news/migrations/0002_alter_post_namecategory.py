# Generated by Django 4.0.4 on 2022-04-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nameCategory',
            field=models.CharField(choices=[('A', 'Article'), ('N', 'News')], default='N', max_length=1),
        ),
    ]
