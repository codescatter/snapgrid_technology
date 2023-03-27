from django.contrib import admin
from .models import Contact, Query, About, Home_Service, Logo, Php_intern, python_intern, django_intern, java_intern, ml_intern, android_intern, ai_intern, ds_intern

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("message", "website", "phone", "email", "name")[::-1]


@admin.register(Home_Service)
class Home_ServiceAdmin(admin.ModelAdmin):
    list_display = ("description", "heading", "icon")[::-1]


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ("hover_logo", "main_logo")[::-1]


@admin.register(Php_intern)
class Php_internAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "phone", "email", "name")[::-1]


@admin.register(python_intern)
class python_internAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "phone", "email", "name")[::-1]


@admin.register(django_intern)
class django_internAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "phone", "email", "name")[::-1]


@admin.register(ml_intern)
class ml_internAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "phone", "email", "name")[::-1]


@admin.register(android_intern)
class android_internAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "phone", "email", "name")[::-1]


@admin.register(ai_intern)
class ai_internAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "phone", "email", "name")[::-1]


@admin.register(ds_intern)
class ds_internAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "phone", "email", "name")[::-1]


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ("message", "website", "phone", "email", "name")[::-1]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("message", "website", "phone", "email", "name")[::-1]


@admin.register(java_intern)
class java_internAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "phone", "email", "name")[::-1]
