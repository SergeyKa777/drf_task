# Generated by Django 2.2.5 on 2019-10-11 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0006_auto_20191011_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ss',
            name='children',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='resttest.Ss'),
        ),
    ]