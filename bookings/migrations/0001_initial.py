# Generated by Django 2.0.4 on 2018-04-30 19:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingLine',
            fields=[
                ('BookingLineId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('departureDate', models.DateTimeField(verbose_name=datetime.datetime(2018, 4, 30, 19, 27, 57, 109959, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('BookingId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bookingDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('bookingType', models.CharField(max_length=50)),
                ('bookingPayment', models.CharField(max_length=30, verbose_name='Payment')),
                ('bookingDeposit', models.CharField(max_length=30, verbose_name='Payment')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('tripId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=200)),
                ('duration', models.TextField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('totalCost', models.CharField(max_length=10)),
                ('hotelName', models.CharField(max_length=100)),
            ],
        ),
    ]