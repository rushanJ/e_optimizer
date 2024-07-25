# Generated by Django 4.2 on 2024-07-14 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customercategorykeyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='search_intrest_string',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='customercategorykeyword',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='customercategory',
            name='searches',
            field=models.IntegerField(default=1),
        ),
    ]