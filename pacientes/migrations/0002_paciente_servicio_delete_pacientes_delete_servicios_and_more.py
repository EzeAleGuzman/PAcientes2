# Generated by Django 4.2.3 on 2023-07-11 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('habitacion', models.CharField(max_length=80)),
                ('cama', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='Pacientes',
        ),
        migrations.DeleteModel(
            name='Servicios',
        ),
        migrations.AddField(
            model_name='paciente',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.servicio'),
        ),
    ]
