# Generated by Django 3.2.7 on 2022-02-04 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True,
                 default='Anonymous', max_length=14, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True,
                 max_length=140, null=True, verbose_name='Body')),
                ('created at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created Datetime'
                )),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
