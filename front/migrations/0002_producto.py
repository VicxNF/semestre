# Generated by Django 4.0.5 on 2022-06-02 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Nombre del producto')),
                ('nombreProducto', models.CharField(max_length=60, verbose_name='Nombre del producto')),
                ('imagen', models.CharField(max_length=100, verbose_name='Imagen del producto')),
                ('precio', models.IntegerField(verbose_name='Precio del producto')),
                ('stock', models.IntegerField(verbose_name='Stock del producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.categoria')),
            ],
        ),
    ]