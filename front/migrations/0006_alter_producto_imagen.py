# Generated by Django 4.0.5 on 2022-07-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos/'),
        ),
    ]
