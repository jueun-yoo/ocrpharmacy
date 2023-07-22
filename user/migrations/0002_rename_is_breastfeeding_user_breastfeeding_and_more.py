# Generated by Django 4.2.3 on 2023-07-22 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0002_alter_recommendedintake_gender'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_breastfeeding',
            new_name='breastfeeding',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_pregnant',
            new_name='pregnant',
        ),
        migrations.AddField(
            model_name='user',
            name='recommended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='supplements.recommendedintake'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', '남성'), ('F', '여성')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserTotalIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_intake', models.FloatField(default=0.0)),
                ('nutrient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.recommendedintake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSupplement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('supplement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_supplements', to='supplements.supplement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_supplements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
