# Generated by Django 2.2.5 on 2019-10-11 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0008_auto_20191011_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ss',
            name='children',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fff', to='resttest.Ss'),
        ),
    ]
