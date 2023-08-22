# Generated by Django 4.2.3 on 2023-08-21 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplements', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='supplement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplement', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recommendednutrient',
            name='nutrient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.nutrient'),
        ),
        migrations.AddField(
            model_name='recommendednutrient',
            name='recommended_intake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.recommendedintake'),
        ),
        migrations.AddField(
            model_name='recommendedintake',
            name='nutrients',
            field=models.ManyToManyField(through='supplements.RecommendedNutrient', to='supplements.nutrient'),
        ),
        migrations.AddField(
            model_name='interaction',
            name='nutrient1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions_nutrient1', to='supplements.nutrient'),
        ),
        migrations.AddField(
            model_name='interaction',
            name='nutrient2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions_nutrient2', to='supplements.nutrient'),
        ),
    ]
