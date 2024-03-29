# Generated by Django 4.1.7 on 2023-03-30 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choise',
            name='is_true',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='choise',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
