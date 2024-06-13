# Generated by Django 4.1.7 on 2023-06-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('paypal', 'Paypal'), ('credit_card', 'Carta di credito'), ('bank_transfer', 'Bonifico bancario')], max_length=20),
        ),
    ]
