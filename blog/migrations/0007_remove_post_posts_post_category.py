# Generated by Django 4.1 on 2022-08-30 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_options_post_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category'),
            preserve_default=False,
        ),
    ]
