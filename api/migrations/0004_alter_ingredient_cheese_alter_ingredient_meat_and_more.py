# Generated by Django 4.1 on 2024-02-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customerdetail_ingredient_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='cheese',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='meat',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='salad',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
