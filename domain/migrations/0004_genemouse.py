# Generated by Django 2.2.24 on 2023-02-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_auto_20200810_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneMouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ensembl_id', models.CharField(max_length=20)),
                ('gene_symbol', models.CharField(db_index=True, max_length=20)),
            ],
        ),
    ]