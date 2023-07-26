from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users', views.UserList.as_view(), name='users_list'),
    path('api/v1/houses', views.HouseAPIView.as_view(), name='houses_list'),
    path('api/v1/houses/<int:pk>/', views.HouseDetailView.as_view(), name='houses_detail'),
    path('api/v1/spells', views.spell_api_view, name='spell_list'),
    path('api/v1/spells/<int:pk>/', views.spell_detail_view, name='spell_detail'),
]   