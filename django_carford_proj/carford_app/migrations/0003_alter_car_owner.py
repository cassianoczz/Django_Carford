# Generated by Django 4.1.4 on 2022-12-14 10:56

import carford_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carford_app', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carford_app.owner', validators=[carford_app.models.restrict_amount]),
        ),
    ]
