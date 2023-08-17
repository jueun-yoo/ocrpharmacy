# Generated by Django 4.2.3 on 2023-08-17 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('unit', models.TextField()),
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
                ('unit', models.CharField(default='TEMP', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
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
                ('unit', models.CharField(default='TEMP', max_length=10)),
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
