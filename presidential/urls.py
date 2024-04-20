from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home_page ,name="homePage"),
    path('reg/',views.register_user, name="register"),
    path('log/', views.login_user, name="login"),
    path('out/', views.logout_user, name="logout"),
    path('prof/<user_id>', views.profile_user, name="profile"),
    path('delete/<user_id>', views.delete_desc, name="delete_desc"),
    path('edit/<user_id>', views.edit_desc, name="edit_desc"),
    path('apply/<user_id>', views.apply_presid, name="apply_presid"),
    path('unapply/<user_id>', views.uncandidate, name="uncandidate"),
]
