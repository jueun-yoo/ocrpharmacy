# Generated by Django 4.2.3 on 2023-07-22 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], max_length=1)),
                ('age_start', models.IntegerField()),
                ('age_end', models.IntegerField()),
                ('pregnant', models.BooleanField()),
                ('breastfeeding', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedNutrient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nutrient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='synonyms', to='supplements.nutrient')),
            ],
        ),
        migrations.CreateModel(
            name='SupplementNutrient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.FloatField(default=0.0)),
                ('nutrient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.nutrient')),
                ('supplement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.supplement')),
            ],
        ),
        migrations.AddField(
            model_name='supplement',
            name='nutrients',
            field=models.ManyToManyField(through='supplements.SupplementNutrient', to='supplements.nutrient'),
        ),
    ]
