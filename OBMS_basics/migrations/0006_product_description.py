# Generated by Django 4.0.4 on 2022-06-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OBMS_basics', '0005_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='This is a test product Lorem ipsum dolor sit amet consectetur adipisicing elit. Et dolor suscipit libero eos atque quia ipsa sint voluptatibus! Beatae sit assumenda asperiores iure at maxime atque repellendus maiores quia sapiente.'),
            preserve_default=False,
        ),
    ]