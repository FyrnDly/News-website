# Generated by Django 4.1.2 on 2022-11-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indonesia', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('ekonomi', 'Ekonomi'), ('sosial-dan-budaya', 'Sosial Budaya'), ('pendidikan', 'Pendidikan'), ('pemerintahan', 'Pemerintah'), ('lainnya', 'Lainnya')], default='lainnya', max_length=255),
        ),
    ]
