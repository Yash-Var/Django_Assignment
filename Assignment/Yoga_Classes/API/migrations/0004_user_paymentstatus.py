# Generated by Django 4.1.1 on 2022-12-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_remove_user_paymentstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='paymentStatus',
            field=models.BooleanField(default=False),
        ),
    ]