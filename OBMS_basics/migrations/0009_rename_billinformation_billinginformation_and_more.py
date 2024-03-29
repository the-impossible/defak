# Generated by Django 4.0.4 on 2022-07-01 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OBMS_basics', '0008_billinformation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BillInformation',
            new_name='BillingInformation',
        ),
        migrations.AddField(
            model_name='order',
            name='billingInformation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBMS_basics.billinginformation'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('session_id', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBMS_basics.payment'),
        ),
    ]
