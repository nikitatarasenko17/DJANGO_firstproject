# Generated by Django 3.2.5 on 2021-07-27 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_visitors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Visitors', to='myapp.visitors'),
        ),
    ]
