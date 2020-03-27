# Generated by Django 2.2.5 on 2020-03-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0015_auto_20200226_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacientes',
            name='banco',
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='cheque',
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='fecha_cheque',
        ),
        migrations.AddField(
            model_name='anticipos',
            name='banco',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='anticipos',
            name='cheque',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='anticipos',
            name='fecha_cheque',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='abono_inicial',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
