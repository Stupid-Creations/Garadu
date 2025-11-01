from django.urls import path

from . import views

urlpatterns = [
    path('report/', views.create_report, name='create_report'),
    path('report/report-success/', views.report_success, name='report_success'),
]