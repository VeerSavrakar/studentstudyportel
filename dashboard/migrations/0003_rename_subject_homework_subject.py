# Generated by Django 4.2.3 on 2024-12-02 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_notes_options_homework'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='Subject',
            new_name='subject',
        ),
    ]