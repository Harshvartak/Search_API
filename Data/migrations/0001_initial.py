# Generated by Django 3.0.5 on 2020-07-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.TextField(blank=True)),
                ('bank_id', models.IntegerField(blank=True, null=True)),
                ('branch', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('district', models.TextField(blank=True)),
                ('state', models.TextField(blank=True)),
                ('bank_name', models.TextField(blank=True)),
            ],
        ),
    ]
