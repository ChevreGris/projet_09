# Generated by Django 4.0.2 on 2022-03-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litreview_app', '0002_ticket_user_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(),
        ),
    ]
