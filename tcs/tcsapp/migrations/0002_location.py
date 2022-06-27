# Generated by Django 4.0.5 on 2022-06-23 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tcsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, null=True)),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcsapp.theatre')),
            ],
        ),
    ]