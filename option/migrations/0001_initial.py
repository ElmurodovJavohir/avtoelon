# Generated by Django 3.2 on 2024-02-07 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('Single', 'Single'), ('Extended', 'Extended'), ('Choice', 'Choice'), ('Button', 'Button'), ('Text', 'Text'), ('Number', 'Number'), ('Multiple choice', 'Multiple Choice')], max_length=15)),
                ('is_extended', models.BooleanField(default=False)),
                ('is_main_filter', models.BooleanField(default=False)),
                ('is_advanced_filter', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OptionValueExtended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OptionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=256)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='option.option')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]