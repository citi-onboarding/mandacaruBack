# Generated by Django 2.0.1 on 2018-02-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_member_patroc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='foto',
            field=models.ImageField(upload_to='membros/'),
        ),
        migrations.AlterField(
            model_name='patroc',
            name='foto',
            field=models.ImageField(upload_to='patrocinadores/'),
        ),
    ]