from django.contrib import admin
from .models import Project, Metric, Manager, Evaluation

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'ty', 'size', 'methodology', 'manager', 'description')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone')

class MetricAdmin(admin.ModelAdmin):
    list_display = ('name', 'ty', 'description')

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('manager', 'metric', 'grade', 'comment')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Metric, MetricAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Evaluation, EvaluationAdmin)