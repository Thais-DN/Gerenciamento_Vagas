# Generated by Django 5.0 on 2023-12-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='nicho_mercado',
            field=models.CharField(choices=[('M', 'Marketing'), ('N', 'Nutrição'), ('D', 'Design'), ('T', 'Tecnologia'), ('E', 'Estetica Canina')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]
