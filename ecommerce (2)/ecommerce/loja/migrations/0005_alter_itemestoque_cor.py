# Generated by Django 5.0.6 on 2024-07-22 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_cor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemestoque',
            name='cor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='loja.cor'),
        ),
    ]
