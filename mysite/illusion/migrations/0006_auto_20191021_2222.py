# Generated by Django 2.2.6 on 2019-10-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('illusion', '0005_auto_20191018_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_db',
            name='age',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='member_db',
            name='gender',
            field=models.CharField(max_length=45),
        ),
    ]
