# Generated by Django 2.2.2 on 2019-07-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20190721_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=10),
        ),
    ]
