from django.db import models


# Create your models here.

class Socialmedia(models.Model):
    social_name = models.CharField(max_length=200, null=True, blank=True)
    facebook_link = models.CharField(max_length=200, null=True, blank=True)
    tweeter_link = models.CharField(max_length=200, null=True, blank=True)
    instagram_link = models.CharField(max_length=200, null=True, blank=True)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.social_name)


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    social = models.OneToOneField(Socialmedia, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='images/customers/', null=True, blank=True)

    def __str__(self):
        return self.first_name


class Marchent(models.Model):
    Owner_name = models.CharField(max_length=100)
    no_of_res = models.IntegerField(null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    social = models.OneToOneField(Socialmedia, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/marchents/')
    nid = models.CharField(max_length=100)
    nid_driving_lic_image = models.ImageField(upload_to='images/nid_dri_lic/')
    reg_date = models.DateTimeField(auto_now_add=True)
    validation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Owner_name


class Restaurant(models.Model):
    mar_id = models.OneToOneField(Marchent, on_delete=models.CASCADE, null=True, blank=True)
    res_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/logo/')
    banner = models.ImageField(upload_to='images/banners/')
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    lat = models.CharField(max_length=500)
    long = models.CharField(max_length=500)
    social = models.OneToOneField(Socialmedia, on_delete=models.CASCADE)
    trade_lic_no = models.CharField(max_length=200)
    trade_lic_image = models.ImageField(upload_to='images/trade_lic/')
    lic_validity_date = models.DateTimeField(null=True, blank=True)
    res_validation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.res_name
