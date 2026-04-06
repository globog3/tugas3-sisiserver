from django.contrib import admin
from .models import Course, Lesson, Category, Enrollment, Progress, User

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'category')
    search_fields = ('title',)
    list_filter = ('category',)
    inlines = [LessonInline]

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Enrollment)
admin.site.register(Progress)
# Register your models here.
