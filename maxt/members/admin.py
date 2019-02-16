from django.contrib import admin
from django.contrib.auth.models import User

from .models import Member

admin.site.unregister(User)

class MemberInline(admin.StackedInline):
    model = Member


@admin.register(User)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = [MemberInline, ]

