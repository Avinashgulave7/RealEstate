# Generated by Django 3.1.2 on 2020-10-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20201015_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='Electricity',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=20),
        ),
        migrations.AlterField(
            model_name='buy',
            name='Lift',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=20),
        ),
    ]
