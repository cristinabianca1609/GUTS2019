# Generated by Django 2.2.6 on 2019-10-19 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_waste_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userproduct',
            old_name='barcode_id',
            new_name='barcode',
        ),
        migrations.RenameField(
            model_name='userproduct',
            old_name='user_id',
            new_name='user',
        ),
    ]