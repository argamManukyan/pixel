from django.contrib import admin

from .models import *


class FooterIconTabularInline(admin.TabularInline):

    model = FooterIcon
    extra = 2


class VacancyTeamImagesTabularInline(admin.TabularInline):

    model = VacancyTeamImages
    extra = 2
    
    
class VacancyAdmin(admin.ModelAdmin):

    inlines = [VacancyTeamImagesTabularInline]




class PortfolioImagesTabularInline(admin.TabularInline):

    model = PortfolioVideoUploads
    extra = 2

class ServicesItemTabInline(admin.StackedInline):

    model = ServiceItem
    extra = 1


class ServiceAdmin(admin.ModelAdmin):

    inlines =  [ServicesItemTabInline]


admin.site.register(HomePage)
admin.site.register(ContactUs)
admin.site.register(TextContext)

admin.site.register(PortfolioCategory)
admin.site.register(Service,ServiceAdmin)
admin.site.register(ServiceCategory,)

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImagesTabularInline]

admin.site.register(Portfolio,PortfolioAdmin)
class FooterDataAdmin(admin.ModelAdmin):
    inlines = [FooterIconTabularInline]

admin.site.register(FooterData,FooterDataAdmin)


# admin.site.register(VacancyItem)
admin.site.register(VacancySubscribe)
admin.site.register(Vacancies,VacancyAdmin)

admin.site.register(Teachers)
admin.site.register(AboutUs)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(Partners)
admin.site.register(ProgrammingLanguages)