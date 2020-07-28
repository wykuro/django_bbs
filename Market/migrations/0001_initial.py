# Generated by Django 2.2.5 on 2020-02-02 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBS_goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('photo1', models.ImageField(upload_to='Market/')),
                ('photo2', models.ImageField(upload_to='Market/')),
                ('photo3', models.ImageField(upload_to='Market/')),
                ('view_count', models.IntegerField()),
                ('content', models.TextField()),
                ('prices', models.CharField(max_length=64)),
                ('tel', models.CharField(max_length=64)),
                ('time', models.CharField(max_length=64)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
