# Generated by Django 4.2.1 on 2023-05-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('alcohol', models.IntegerField()),
                ('speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vibration', models.IntegerField()),
                ('x_acceleration', models.IntegerField()),
                ('y_acceleration', models.IntegerField()),
                ('z_acceleration', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]