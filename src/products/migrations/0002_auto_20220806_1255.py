# Generated by Django 3.2.14 on 2022-08-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productType',
            new_name='product_type',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='product',
            name='doc',
            field=models.FileField(default='Doc/None/No-doc.pdf', upload_to='Doc/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/'),
        ),
    ]