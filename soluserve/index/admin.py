from django.contrib import admin
from .models import CSR, IMS, ESG, Capabilities, Career, Experience, PartnersLogo, PartnersText, ProductSupplied, SerivesRendered, Services, WhoWeAreHome, WhoWeAreAbout, WEDS, WSPS


# Who We Are - Home
class WhoWeAreHomeAdmin(admin.ModelAdmin):
    search_fields = ['summary', '']
    list_display = ['summary']


admin.site.register(WhoWeAreHome, WhoWeAreHomeAdmin)


# Who We Are - About
class WhoWeAreAboutAdmin(admin.ModelAdmin):
    search_fields = ['description', '']
    list_display = ['description']


admin.site.register(WhoWeAreAbout, WhoWeAreAboutAdmin)

# Services


class ServicesAdmin(admin.ModelAdmin):
    search_fields = ['title', 'summary', '']
    list_display = ['id', 'title', 'image']


admin.site.register(Services, ServicesAdmin)

# Capabilities


class CapabilitiesAdmin(admin.ModelAdmin):
    search_fields = ['title', '']
    list_display = ['title']


admin.site.register(Capabilities, CapabilitiesAdmin)

# PartnersLogo


class PartnerLogoAdmin(admin.ModelAdmin):
    search_fields = ['name', '']
    list_display = ['name', 'logo']


admin.site.register(PartnersLogo, PartnerLogoAdmin)

# IMS


class IMSAdmin(admin.ModelAdmin):
    search_fields = ['description', '']
    list_display = ['description']


admin.site.register(IMS, IMSAdmin)

# ESG


class ESGAdmin(admin.ModelAdmin):
    search_fields = ['description', '']
    list_display = ['description']


admin.site.register(ESG, ESGAdmin)

# CSR


class CSRAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', '']
    list_display = ['title', 'description', 'image']


admin.site.register(CSR, CSRAdmin)

# ServicesRendered


class ServicesRenderedAdmin(admin.ModelAdmin):
    search_fields = ['description', '']
    list_display = ['description']


admin.site.register(SerivesRendered, ServicesRenderedAdmin)

# PartnersText


class PartnerTextAdmin(admin.ModelAdmin):
    search_fields = ['title', '']
    list_display = ['title', 'summary']


admin.site.register(PartnersText, PartnerTextAdmin)

# ProductSupplied


class ProductSuppliedAdmin(admin.ModelAdmin):
    search_fields = ['description', '']
    list_display = ['description']


admin.site.register(ProductSupplied, ProductSuppliedAdmin)

# Experience


class ExperienceAdmin(admin.ModelAdmin):
    search_fields = ['description', '']
    list_display = ['description']


admin.site.register(Experience, ExperienceAdmin)

# WEDS


class WEDSAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', '']
    list_display = ['title', 'description']


admin.site.register(WEDS, WEDSAdmin)

# WSPS


class WSPSAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', '']
    list_display = ['title', 'description']


admin.site.register(WSPS, WSPSAdmin)

# Careers


class CareersAdmin(admin.ModelAdmin):
    search_fields = ['job_title', 'job_type',
                     'job_location' 'experience_level', '']
    list_display = ['id', 'job_title', 'job_type',
                    'job_location', 'experience_level', 'job_summary']


admin.site.register(Career, CareersAdmin)
