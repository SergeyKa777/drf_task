# Generated by Django 2.2.5 on 2019-10-11 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0005_auto_20191011_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ss',
            name='children',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='resttest.Ss'),
            preserve_default=False,
        ),
    ]
