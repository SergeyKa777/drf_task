# Generated by Django 2.2.5 on 2019-10-11 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0003_probe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('children', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resttest.Ss')),
            ],
        ),
    ]
