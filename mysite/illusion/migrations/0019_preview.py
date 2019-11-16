# Generated by Django 2.2.6 on 2019-11-02 07:04

from django.db import migrations, models
import illusion.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('illusion', '0018_delete_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.FileField(null=True, upload_to=illusion.file_upload.file_upload_path)),
                ('style_id', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
    ]
