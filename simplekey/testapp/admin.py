from django.contrib import admin
from .models import Buy,Rent,Land,Agent,RentImage,BuyImage,LandImage,Contact,Select_Property

# class BuyAdmin1(admin.ModelAdmin):
#     list_display = ['id','gallary','Owner_name','Contact','Property_name','Property','Type','Rooms','Baths','Area','Water','Playground','Price','Description','Gym','Hospital','School','Mall','Pincode','State','City','Address','Img1','Electricity','Parking','Club','Fire','Lift','Wifi','Security','Temple','Poll','Living','Hotel','Cinema','Date']

# class RentAdmin(admin.ModelAdmin):
#     list_display = ['Owner_name','Contact','Property_name','Property','Type','Rooms','Baths','Area','Water','Playground','Price','Description','Gym','Hospital','School','Mall','Pincode','State','City','Address','Img1','Electricity','Parking','Club','Fire','Lift','Wifi','Security','Temple','Poll','Living','Hotel','Cinema','Date']

# Register your models here.


class RentImageInline(admin.TabularInline):
    model = RentImage
    extra = 3


class RentAdmin(admin.ModelAdmin):
    inlines = [ RentImageInline, ]
    list_display = ['Owner_name', 'Contact', 'Property_name', 'Property', 'Type', 'Rooms', 'Baths', 'Area', 'Water',
                    'Playground', 'Price', 'Description', 'Gym', 'Hospital', 'School', 'Mall', 'Pincode', 'State',
                    'City', 'Address', 'Img1', 'Electricity', 'Parking', 'Club', 'Fire', 'Lift', 'Wifi', 'Security',
                    'Temple', 'Poll', 'Living', 'Hotel', 'Cinema', 'Date']

    list_filter = ('Price', 'Date')

    search_fields = ('Property_name', 'Address', 'State', 'City', 'Pincode')


admin.site.register(Rent, RentAdmin)

class BuyImageInline(admin.TabularInline):
    model = BuyImage
    extra = 3

class BuyAdmin(admin.ModelAdmin):
    inlines = [ BuyImageInline, ]
    list_display = ['Owner_name', 'Contact', 'Property_name', 'Property', 'Type', 'Rooms', 'Baths', 'Area', 'Water',
                    'Playground', 'Price', 'Description', 'Gym', 'Hospital', 'School', 'Mall', 'Pincode', 'State',
                    'City', 'Address', 'Img1', 'Electricity', 'Parking', 'Club', 'Fire', 'Lift', 'Wifi', 'Security',
                    'Temple', 'Poll', 'Living', 'Hotel', 'Cinema', 'Date']

    list_filter = ('Price','Date')

    search_fields = ('Property_name','Address','State','City','Pincode')


admin.site.register(Buy, BuyAdmin)


class LandImageInline(admin.TabularInline):
    model = LandImage
    extra = 3

class LandAdmin(admin.ModelAdmin):
    inlines = [ LandImageInline, ]
    list_display = ['Owner_name','Contact','Property','Property_type','Price','Area','Description','Document','Tax_Raciept'
        ,'Survey_Sketch','Pincode','State','City','Address','Img1','Date']

    list_filter = ('Price', 'Date')

    search_fields = ('Address', 'State', 'City', 'Pincode')


admin.site.register(Land, LandAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

    search_fields = ('name','email')

admin.site.register(Contact,ContactAdmin)

class AgentAdmin(admin.ModelAdmin):
    list_display = ['Agent_name','Contact','Email','Agent_type','Img1']
    search_fields = ('Agent_name','Contact','Email')

admin.site.register(Agent,AgentAdmin)


class Select_Property_Admin(admin.ModelAdmin):
    list_display = ['name','email','mobile','date','property','msg']
    search_fields = ('name','email')
    list_filter = ('date',)

    change_form_template = 'admin/testapp/change_form.html'


admin.site.register(Select_Property,Select_Property_Admin)








