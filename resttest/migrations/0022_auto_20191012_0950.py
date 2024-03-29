# Generated by Django 2.2.5 on 2019-10-12 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0021_auto_20191012_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ss',
            name='parentid',
        ),
        migrations.AddField(
            model_name='ss',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='resttest.Ss'),
        ),
        migrations.AlterField(
            model_name='ss',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='ss',
            table=None,
        ),
    ]
