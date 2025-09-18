from django.contrib import admin
from .models import Course, Category, Enrollment, Profile

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','instructor','fee','published')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Enrollment)
admin.site.register(Profile)