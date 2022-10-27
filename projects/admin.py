from django.contrib import admin

from .models import Project, ProjectFacility, HouseType, HouseFeature

# Register your models here.


@admin.register(HouseFeature)
class HouseFeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(HouseType)
class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ['house_name', 'project', 'house_specification', 'house_floor_area','units']

class HouseTypeInline(admin.StackedInline): # new
   model = HouseType




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
   
   list_display = ['name', 'hectares','purpose','location', 'status']
   inlines = [
            HouseTypeInline,
]


    

@admin.register(ProjectFacility)
class HouseFacilityAdmin(admin.ModelAdmin):
    pass