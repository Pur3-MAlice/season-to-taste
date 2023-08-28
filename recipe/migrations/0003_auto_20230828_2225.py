# Generated by Django 3.2.20 on 2023-08-28 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0002_auto_20230828_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='SavedRecipe',
        ),
    ]
