# Generated by Django 4.2.1 on 2023-05-13 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieDataApp', '0003_alter_moviedata_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='reviews_from_critics',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moviedata',
            name='reviews_from_user',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
