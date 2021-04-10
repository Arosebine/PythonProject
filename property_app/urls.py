from django.urls import path
from property_app import views


app_name='property_app'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('agent-page/', views.agents, name='agents'),
    path('agent-dashboard-page/', views.agent_dashboard, name='agent_dashboard'),
]
