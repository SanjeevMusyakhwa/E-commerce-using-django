# Generated by Django 5.1.3 on 2024-11-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_cartorderitems_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorderitems',
            old_name='quantity4',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='cartorderitems',
            name='invoice_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]