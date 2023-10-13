# Generated by Django 4.2.6 on 2023-10-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_bottle',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_container',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_pack',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_pouch',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='volume_in_cl',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='volume_in_lt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='volume_in_ml',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight_in_grams',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight_in_kgs',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]