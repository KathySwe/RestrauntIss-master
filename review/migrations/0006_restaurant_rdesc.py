# Generated by Django 2.1.7 on 2019-07-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20190720_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='Rdesc',
            field=models.CharField(max_length=300, null=True),
        ),
    ]