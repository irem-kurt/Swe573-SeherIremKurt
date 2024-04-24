# Generated by Django 4.2.1 on 2024-04-23 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('location', location_field.models.plain.PlainLocationField(default='41.0255493,28.9742571', max_length=63)),
                ('picture', models.ImageField(default='uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures/')),
                ('unreadcount', models.IntegerField(default=0)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
