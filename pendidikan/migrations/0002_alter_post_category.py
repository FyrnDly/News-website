# Generated by Django 4.1.2 on 2022-11-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendidikan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('beasiswa', 'Beasiswa'), ('sekolah', 'Sekolah'), ('perguruan-tinggi', 'Perguruan Tinggi'), ('kemendikbudristek', 'Kemendikbudristek'), ('lainnya', 'Lainnya')], default='lainnya', max_length=255),
        ),
    ]
