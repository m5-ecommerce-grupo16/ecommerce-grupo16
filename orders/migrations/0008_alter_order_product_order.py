# Generated by Django 4.0.7 on 2023-03-10 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_product_ammount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_product',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summary', to='orders.order'),
        ),
    ]
