# Generated by Django 2.2.6 on 2019-10-15 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('illusion', '0002_auto_20191014_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_db',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
