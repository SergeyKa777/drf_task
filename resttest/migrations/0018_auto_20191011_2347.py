# Generated by Django 2.2.5 on 2019-10-11 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0017_children_ss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='children',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ss',
            name='children',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resttest.Children'),
        ),
    ]
