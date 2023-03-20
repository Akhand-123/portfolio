from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)


class InternshipAdmin(admin.ModelAdmin):
    List_display=('fullname'
    'usn'
    'email'
    'collage_name'
    'offer_status'
    'start_date'
    'end_date'
    'proj_report')
    search_fields=('fullname','usn','email')
    list_filter=('collage_name','offer_status','proj_report')

admin.site.register(Internship,InternshipAdmin)

    
    
    