from django.db import models

# Create your models here.
class Slider(models.Model):
        slider_desc = models.TextField()
        slider_head = models.CharField(max_length=100)
        slider_btn = models.CharField(max_length=50)
        slider_image = models.ImageField(upload_to='slides/')

        def __str__(self):
            return self.slider_head

class Featured(models.Model):
    feature_desc = models.TextField()
    feature_title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.feature_title

class About(models.Model):
    about_title = models.CharField(max_length=255)
    about_desc = models.TextField()

    def __str__(self):
        return self.about_title

class Info(models.Model):
    info_title = models.CharField(max_length=255)
    info_description = models.TextField()
    info_image = models.ImageField(upload_to='info/', blank=True, null=True)
    info_feature_1 = models.TextField()
    info_feature_2 = models.TextField()
    info_feature_3 = models.TextField()
    info_desc_2 = models.TextField()

    def __str__(self):
        return self.info_title


class Sections(models.Model):
    sect_num = models.IntegerField()
    sect_title = models.CharField(max_length=255)
    sect_desc = models.TextField()


    def __str__(self):
        return self.sect_title


class Service(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title