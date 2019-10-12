# Generated by Django 2.2.5 on 2019-10-11 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0009_auto_20191011_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ss',
            name='children',
        ),
        migrations.AddField(
            model_name='ss',
            name='parrent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='resttest.Ss'),
        ),
    ]
