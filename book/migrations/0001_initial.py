# Generated by Django 4.2.5 on 2023-09-25 01:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('edition', models.PositiveSmallIntegerField()),
                ('publication_year', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
