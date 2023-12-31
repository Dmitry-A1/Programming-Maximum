from django.contrib import admin
from .models import Advertisement
# Register your models here.

class Advirtisement_admin(admin.ModelAdmin):
    list_display = ['id','title','description','updated_at_date','price','auction','created_date']
    list_filter = ['auction','created_at']
    actions = ['make_auction_as_false','make_auction_as_true']
    fieldsets = [
        ('Общие', {
            'fields':('title','description'),
        }),
        ('Финансы',{
            'fields':('price','auction'),
            'classes':['collapse']
        })
    ]
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self,request,queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
admin.site.register(Advertisement, Advirtisement_admin)