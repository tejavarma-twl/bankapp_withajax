# Generated by Django 2.2.6 on 2019-10-28 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_name', models.CharField(default='', max_length=30)),
                ('beneficiary_accno', models.BigIntegerField(blank=True, null=True)),
                ('ifsc_code', models.CharField(default='', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
