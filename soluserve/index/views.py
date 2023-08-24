from django.shortcuts import render
from .models import CSR, ESG, IMS, WEDS, WSPS, Capabilities, Career, Experience, PartnersLogo, PartnersText, ProductSupplied, SerivesRendered, Services, WhoWeAreAbout, WhoWeAreHome
from django.views import View


class IndexView(View):
    template_index = 'index.html'

    def get(self, request):
        wwah = WhoWeAreHome.objects.all()
        services = Services.objects.all()
        capabilities = Capabilities.objects.all()
        partnerslogos = PartnersLogo.objects.all()
        return render(request, self.template_index, {
            'wwahs': wwah,
            'services': services,
            'capabilities': capabilities,
            'partnerslogos': partnerslogos
        })


class WhoWeAreView(View):
    template_whoweare = 'whoweare.html'

    def get(self, request):
        wwaa = WhoWeAreAbout.objects.all()
        sevrend = SerivesRendered.objects.all()
        parttext = PartnersText.objects.all()
        products = ProductSupplied.objects.all()
        return render(request, self.template_whoweare, {
            'wwaas': wwaa,
            'sevrendz': sevrend,
            'parttexts': parttext,
            'productzs': products
        })


class CopStructureView(View):
    template_copstructure = 'cop-structure.html'

    def get(self, request):
        return render(request, self.template_copstructure, {})


class ExperienceView(View):
    template_experience = 'experience.html'

    def get(self, request):
        experiences = Experience.objects.all()
        return render(request, self.template_experience, {'experiences': experiences})


class QHSEView(View):
    template_qhse = 'qhse.html'

    def get(self, request):
        ims = IMS.objects.all()
        esg = ESG.objects.all()
        return render(request, self.template_qhse, {
            'ims': ims,
            'esg': esg
        })


class CSRView(View):
    template_csr = 'csr.html'

    def get(self, request):
        csr = CSR.objects.all()
        return render(request, self.template_csr, {'csr': csr})


class ServicesView(View):
    template_services = 'services.html'

    def get(self, request):
        weds = WEDS.objects.all()
        wsps = WSPS.objects.all()
        return render(request, self.template_services, {
            'weds': weds,
            'wsps': wsps
        })


class CareersView(View):
    template_careers = 'careers.html'

    def get(self, request):
        careers = Career.objects.all()
        return render(request, self.template_careers, {'careers': careers})


class MediaView(View):
    template_media = 'media.html'

    def get(self, request):
        return render(request, self.template_media, {})


class ContactUsView(View):
    template_contactus = 'contact-us.html'

    def get(self, request):
        return render(request, self.template_contactus, {})
