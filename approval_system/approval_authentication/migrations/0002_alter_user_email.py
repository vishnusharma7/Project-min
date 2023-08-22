# Generated by Django 3.2.6 on 2023-08-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approval_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=300, null=True, unique=True),
        ),
    ]
