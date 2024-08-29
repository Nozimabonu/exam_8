# Generated by Django 5.0.7 on 2024-08-03 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='texnomart.category')),
                ('users_like', models.ManyToManyField(blank=True, db_table='users_like', related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('is_primary', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_images', to='texnomart.category')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='texnomart.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('positive', models.TextField()),
                ('disadvantage', models.TextField()),
                ('comments', models.TextField()),
                ('rating', models.IntegerField(blank=True, choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=5, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='comments/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='texnomart.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='texnomart.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='texnomart.product')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='texnomart.attributevalue')),
            ],
        ),
    ]
