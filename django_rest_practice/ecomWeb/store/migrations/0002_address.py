# Generated by Django 4.1 on 2022-09-22 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField()),
                ('h_no', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
    ]