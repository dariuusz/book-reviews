# Generated by Django 4.2.2 on 2023-06-26 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_book_contributor_review_bookcontributor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='contibutors',
            new_name='contributors',
        ),
    ]
