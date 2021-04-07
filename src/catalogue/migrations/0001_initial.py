# Generated by Django 3.1.7 on 2021-04-07 13:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, help_text='Brief description of this book.', max_length=10000, null=True)),
                ('isbn', models.CharField(help_text='13-digit <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a> for this book.', max_length=13, unique=True, verbose_name='ISBN')),
                ('author', models.ManyToManyField(to='catalogue.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='E.g. Philosophy, Mathematics, Computer Science.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='A unique ID for this copy across the whole library.', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('loan_status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Current availability for this book copy.', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalogue.book')),
            ],
            options={
                'verbose_name_plural': 'Book copies',
                'ordering': ['due_date'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Genre(s) for this book.', to='catalogue.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Language(s) for this book.', to='catalogue.Language'),
        ),
    ]