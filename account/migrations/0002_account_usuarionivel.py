# Generated by Django 3.1.5 on 2021-01-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='UsuarioNivel',
            field=models.CharField(default='basico', max_length=20),
        ),
    ]
