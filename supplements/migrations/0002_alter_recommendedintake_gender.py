# Generated by Django 4.2.3 on 2023-07-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendedintake',
            name='gender',
            field=models.CharField(choices=[('M', '남성'), ('F', '여성')], max_length=1),
        ),
    ]