from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(Setting)
class AdminSetting(admin.ModelAdmin):
    list_filter = ['c_name']
    list_display = ['c_name', 'c_email', 'c_phone', 'c_address']
    search_fields = ['c_name']


    def __str__(self):
        return self.c_name

    def get_company_name(self):
        c_name = str(self.c_name)
        return c_name.title()



@admin.register(Attribute)
class AdminAttribute(admin.ModelAdmin):
    pass


@admin.register(AttributeValue)
class AdminAttributeValue(admin.ModelAdmin):
    pass


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
  pass


@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    pass


@admin.register(ProductAttribute)
class AdminProductAttribute(admin.ModelAdmin):
    pass
