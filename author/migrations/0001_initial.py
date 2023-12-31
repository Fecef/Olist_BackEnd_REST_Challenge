# Generated by Django 4.2.5 on 2023-09-25 01:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('books', models.ManyToManyField(related_name='authors', to='book.book')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
