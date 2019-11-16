# Generated by Django 2.2.6 on 2019-10-28 10:28

from django.db import migrations, models
import illusion.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('illusion', '0007_member_db_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileTest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.FileField(null=True, upload_to=illusion.file_upload.file_upload_path)),
            ],
        ),
    ]
