# Generated by Django 4.0.6 on 2022-07-29 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_hotel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rooms',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('start_period', models.DateField()),
                ('stop_period', models.DateField()),
                ('start_period2', models.DateField()),
                ('stop_period2', models.DateField()),
                ('start_period3', models.DateField()),
                ('stop_period3', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
        ),
    ]
