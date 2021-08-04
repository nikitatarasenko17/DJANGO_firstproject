# Generated by Django 3.2.5 on 2021-07-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_comment_like_post_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='library',
            name='book',
        ),
        migrations.RemoveField(
            model_name='library',
            name='borrower',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='user',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.DeleteModel(
            name='Visitors',
        ),
    ]