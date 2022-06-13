# Generated by Django 4.0.5 on 2022-06-13 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='front.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del producto'),
        ),
    ]
