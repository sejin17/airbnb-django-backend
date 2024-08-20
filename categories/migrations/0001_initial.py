# Generated by Django 5.1 on 2024-08-20 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('type', models.CharField(blank=True, choices=[('rooms', 'Rooms'), ('experiences', 'Experiences')], max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
