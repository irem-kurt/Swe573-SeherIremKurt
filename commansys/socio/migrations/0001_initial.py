# Generated by Django 4.2.1 on 2024-04-14 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
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
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(default='')),
                ('requester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requester', to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('toPerson', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toPerson', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='NotifyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField(blank=True, null=True)),
                ('hasRead', models.BooleanField(default=False)),
                ('offerType', models.TextField(blank=True, null=True)),
                ('offerPk', models.IntegerField(default=0)),
                ('notify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.TextField(default='Community Name', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(default='uploads/service_pictures/default.png', upload_to='uploads/service_pictures/')),
                ('location', location_field.models.plain.PlainLocationField(default='41.0255493,28.9742571', max_length=63)),
                ('is_private', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='socio.tag', verbose_name='category')),
                ('followers', models.ManyToManyField(related_name='followed_communities', to=settings.AUTH_USER_MODEL)),
                ('managers', models.ManyToManyField(related_name='managed_communities', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
