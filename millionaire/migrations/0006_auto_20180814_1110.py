# Generated by Django 2.1 on 2018-08-14 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('millionaire', '0005_auto_20180814_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBestScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.SmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        # migrations.RemoveField(
        #     model_name='userscore',
        #     name='user',
        # ),
        # migrations.DeleteModel(
        #     name='UserScore',
        # ),
    ]