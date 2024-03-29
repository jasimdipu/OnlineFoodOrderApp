# Generated by Django 3.2.4 on 2021-06-09 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marchent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner_name', models.CharField(max_length=100)),
                ('no_of_res', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField()),
                ('image', models.ImageField(upload_to='images/marchents/')),
                ('nid', models.CharField(max_length=100)),
                ('nid_driving_lic_image', models.ImageField(upload_to='images/nid_dri_lic/')),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('validation_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Socialmedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.CharField(blank=True, max_length=200, null=True)),
                ('tweeter_link', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='images/logo/')),
                ('banner', models.ImageField(upload_to='images/banners/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField()),
                ('lat', models.CharField(max_length=500)),
                ('long', models.CharField(max_length=500)),
                ('trade_lic_no', models.CharField(max_length=200)),
                ('trade_lic_image', models.ImageField(upload_to='images/trade_lic/')),
                ('lic_validity_date', models.DateTimeField(blank=True, null=True)),
                ('res_validation_date', models.DateTimeField(blank=True, null=True)),
                ('mar_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodorder.marchent')),
                ('social', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foodorder.socialmedia')),
            ],
        ),
        migrations.AddField(
            model_name='marchent',
            name='social',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foodorder.socialmedia'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField()),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='images/customers/')),
                ('social', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foodorder.socialmedia')),
            ],
        ),
    ]
