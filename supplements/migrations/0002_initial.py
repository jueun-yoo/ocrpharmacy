<<<<<<< HEAD
# Generated by Django 4.2.3 on 2023-08-12 10:48
=======
# Generated by Django 4.2.3 on 2023-08-11 10:27
>>>>>>> dafd6ec6f6ad0c7e30868b8056715a256fa69ad4

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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions1', to='supplements.nutrient'),
        ),
        migrations.AddField(
            model_name='interaction',
            name='nutrient2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions2', to='supplements.nutrient'),
        ),
    ]
