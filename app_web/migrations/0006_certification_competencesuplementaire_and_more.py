# Generated by Django 4.1.1 on 2022-11-22 06:23

from django.db import migrations, models
import django_quill.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0005_info_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('titre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Certification',
            },
        ),
        migrations.CreateModel(
            name='CompetenceSuplementaire',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('titre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'CompetenceSuplementaire',
            },
        ),
        migrations.CreateModel(
            name='FormationAttestee',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('titre', models.CharField(max_length=200)),
                ('entreprise', models.CharField(blank=True, max_length=200, null=True)),
                ('periode', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'FormationAttestee',
            },
        ),
        migrations.CreateModel(
            name='Qualite',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('titre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Qualite',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('titre', models.CharField(max_length=200)),
                ('entreprise', models.CharField(blank=True, max_length=200, null=True)),
                ('periode', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Stage',
            },
        ),
        migrations.AddField(
            model_name='info',
            name='resume',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]