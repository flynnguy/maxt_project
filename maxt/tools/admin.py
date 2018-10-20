from django.contrib import admin

from .models import Tool, Section

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'section', 'wiki_link')

