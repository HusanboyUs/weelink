# Generated by Django 4.0.3 on 2022-03-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_profilelink_link_alter_profilelink_link_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
