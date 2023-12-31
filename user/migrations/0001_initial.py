# Generated by Django 4.2.3 on 2023-08-24 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('남', '남성'), ('여', '여성')], max_length=1)),
                ('pregnant', models.BooleanField(default=False)),
                ('breastfeeding', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='supplements.recommendedintake')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserTotalIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.FloatField(default=0.0)),
                ('unit', models.CharField(default='TEMP', max_length=10)),
                ('nutrient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.nutrient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='totalintake',
            field=models.ManyToManyField(through='user.UserTotalIntake', to='supplements.nutrient'),
        ),
    ]
