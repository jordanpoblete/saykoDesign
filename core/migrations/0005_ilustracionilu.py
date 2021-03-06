# Generated by Django 3.2.3 on 2021-06-15 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210608_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='IlustracionIlu',
            fields=[
                ('idIlustracion', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Ilustracion')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('descripcionIlu', models.CharField(max_length=600, verbose_name='descripcion')),
                ('fecha', models.DateField(verbose_name='fecha')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
