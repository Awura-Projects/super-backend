# Generated by Django 3.2.14 on 2022-08-21 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0002_auto_20220806_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.supplier'),
        ),
        migrations.DeleteModel(
            name='Producer',
        ),
    ]
