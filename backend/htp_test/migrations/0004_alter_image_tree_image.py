# Generated by Django 4.2.4 on 2023-11-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htp_test', '0003_alter_htp_created_date_alter_image_tree_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_tree',
            name='image',
            field=models.ImageField(upload_to='img_tree/'),
        ),
    ]
