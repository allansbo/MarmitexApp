# Generated by Django 3.0.8 on 2020-07-05 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientesapp', '0007_remove_phone_phone_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='phone_client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientesapp.Client'),
            preserve_default=False,
        ),
    ]