from django.urls import path
from . import views

urlpatterns = [
    path('inventories/', views.get_all, name='inventory-list'),
    path('create-inventory/', views.create_inventory, name='inventory-create'),
    path('inventory/<int:id>/', views.get_byid),

    # path('vulnerabilities/summary/', views.vulnerability_severity_summary, name='vulnerability-summary'),
    # path('vulnerabilities/excluding-fixed/', views.get_queryset, name='vulnerability-excluding-fixed'),
]
