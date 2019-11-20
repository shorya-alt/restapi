# Generated by Django 2.2.7 on 2019-11-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userbankdetails', '0004_auto_20191120_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='branch',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='ifsc',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
