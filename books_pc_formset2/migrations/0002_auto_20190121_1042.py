# Generated by Django 2.1.5 on 2019-01-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_pc_formset2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='contribution',
            field=models.IntegerField(choices=[(1, 'Author'), (2, 'EDITOR'), (3, 'REVIEWER')]),
        ),
    ]
