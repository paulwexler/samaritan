# Generated by Django 3.0 on 2021-05-22 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('published', models.DateField(verbose_name='date published')),
            ],
            options={
                'unique_together': {('author', 'title')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='review.Book')),
            ],
        ),
    ]