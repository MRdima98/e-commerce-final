# Generated by Django 4.0.5 on 2022-07-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_hotel_free_time_alter_hotel_cost_alter_hotel_rooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='CAP',
            field=models.DecimalField(decimal_places=0, default=41000, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.TextField(default='modena'),
            preserve_default=False,
        ),
    ]
