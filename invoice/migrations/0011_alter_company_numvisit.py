# Generated by Django 5.0.3 on 2024-08-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_company_hascode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='numvisit',
            field=models.BigIntegerField(default=0),
        ),
    ]
