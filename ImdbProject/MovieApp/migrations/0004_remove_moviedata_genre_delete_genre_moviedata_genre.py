# Generated by Django 4.2.1 on 2023-05-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0003_alter_genre_genrename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedata',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.TextField(null=True),
        ),
    ]