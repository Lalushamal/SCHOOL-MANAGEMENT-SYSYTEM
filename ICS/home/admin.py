from django.contrib import admin
from . models import Register,Course,Attendences,Mark,Attend

class RegisterAdmin(admin.ModelAdmin):
    list_display=('register_no','name','address','age','gender','course','batch_time','phone_no','email')
admin.site.register (Register,RegisterAdmin)
admin.site.register(Course)
class AttendenceAdmin(admin.ModelAdmin):
    list_display=('register_no','year','month','present','absent')
admin.site.register (Attendences,AttendenceAdmin)
class MarkAdmin(admin.ModelAdmin):
    list_display=('register_no','exam_date','mark_theory','mark_pratical')
admin.site.register(Mark,MarkAdmin)
class AttendAdmin(admin.ModelAdmin):
    list_display=('register_no','course','month','year')
admin.site.register (Attend,AttendAdmin)