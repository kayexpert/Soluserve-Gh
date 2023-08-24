from django.db import models


class WhoWeAreHome(models.Model):
    summary = models.TextField(default='')

    def __str__(self):
        return self.summary


class PartnersLogo(models.Model):
    name = models.CharField(max_length=100, default='')
    logo = models.ImageField(upload_to='partners_images')

    def __str__(self):
        return self.name


class WhoWeAreAbout(models.Model):
    description = models.TextField(default='')

    def __str__(self):
        return self.description


class IMS(models.Model):
    # title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.description


class ESG(models.Model):
    # title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.description


class CSR(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    image = models.ImageField(upload_to='csr_images')

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=100, default='')
    summary = models.TextField(default='')
    image = models.ImageField(upload_to='gallery_images')

    def __str__(self):
        return self.title


class Capabilities(models.Model):
    title = models.CharField(max_length=100, default='')
    # image = models.ImageField(upload_to='capabilities_images')

    def __str__(self):
        return self.title


class SerivesRendered(models.Model):
    description = models.TextField(default='')

    def __str__(self):
        return self.description


class PartnersText(models.Model):
    title = models.CharField(max_length=100, default='')
    summary = models.TextField(default='')

    def __str__(self):
        return self.title


class ProductSupplied(models.Model):
    description = models.TextField(default='')

    def __str__(self):
        return self.description


class Experience(models.Model):
    description = models.TextField(default='')

    def __str__(self):
        return self.description


class WEDS(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title


class WSPS(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title


class Career(models.Model):
    job_title = models.CharField(max_length=50, default='')
    job_type = models.CharField(max_length=50, default='')
    job_location = models.CharField(max_length=50, default='')
    experience_level = models.CharField(max_length=50, default='')
    job_summary = models.TextField(default='')

    def __str__(self):
        return self.job_title
