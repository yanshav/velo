# Generated by Django 3.1.5 on 2021-02-03 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0010_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historymarsh',
            name='category',
        ),
        migrations.AddField(
            model_name='historymarsh',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='velo.velomarsh', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]