# Generated by Django 2.0.5 on 2023-12-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('volume', models.FloatField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]