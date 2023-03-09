# Generated by Django 4.1.7 on 2023-03-09 19:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DumperModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название модели')),
                ('dumper_models_unique_name', models.CharField(default=None, max_length=60, unique=True, verbose_name='Название модели')),
                ('maximum_load', models.IntegerField(default=0, verbose_name='Максимальная грузоподъёмность')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='Активен или нет')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'verbose_name': 'Модель машины',
                'verbose_name_plural': 'Модели машин',
                'db_table': 'core_dumper_models',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=100, verbose_name='Номер машины')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='Активен или нет')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('dumper_models', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.dumpermodels')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
                'db_table': 'core_machines',
                'ordering': ['numbers'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Производители')),
                ('manufacturer_unique_name', models.CharField(default=None, max_length=60, unique=True, verbose_name='Название производителя')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='Активен или нет')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
                'db_table': 'core_manufacturer',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MachinesOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_weight_payload', models.IntegerField(default=0, verbose_name='Текущий вес загрузки в Тоннах')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='Актива или нет')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('machines', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.machines')),
            ],
            options={
                'verbose_name': 'Машина в работе',
                'verbose_name_plural': 'Машины в работе',
                'db_table': 'core_machines_operation',
                'ordering': ['machines'],
            },
        ),
        migrations.AddField(
            model_name='machines',
            name='manufacturer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.manufacturer'),
        ),
        migrations.AddField(
            model_name='dumpermodels',
            name='manufacturer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.manufacturer'),
        ),
    ]
