# Generated by Django 4.2.5 on 2023-10-04 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_fruit_cost_alter_fruit_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'all items',
                'verbose_name_plural': 'all items',
                'db_table': 'all_items',
            },
        ),
        migrations.DeleteModel(
            name='Fruit',
        ),
    ]
