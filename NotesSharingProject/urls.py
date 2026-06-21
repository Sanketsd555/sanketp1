from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.userlogin, name='login'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('signup/', views.signup1, name='signup'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('upload_notes/', views.upload_notes, name='upload_notes'),
    path('view_mynotes/', views.view_mynotes, name='view_mynotes'),
    path('delete_mynotes/<int:pid>/', views.delete_mynotes, name='delete_mynotes'),
    path('view_allnotes/', views.view_allnotes, name='view_allnotes'),
    path('view_users/', views.view_users, name='view_users'),
    path('delete_users/<int:pid>/', views.delete_users, name='delete_users'),
    path('pending_notes/', views.pending_notes, name='pending_notes'),
    path('accepted_notes/', views.accepted_notes, name='accepted_notes'),
    path('rejected_notes/', views.rejected_notes, name='rejected_notes'),
    path('all_notes/', views.all_notes, name='all_notes'),
    path('assign_status/<int:pid>/', views.assign_status, name='assign_status'),
    path('delete_notes/<int:pid>/', views.delete_notes, name='delete_notes'),
    path('viewallnotes/', views.viewallnotes, name='viewallnotes'),
    path('change_passwordadmin/', views.change_passwordadmin, name='change_passwordadmin'),
    path('unread_queries/', views.unread_queries, name='unread_queries'),
    path('read_queries/', views.read_queries, name='read_queries'),
    path('view_queries/<int:pid>/', views.view_queries, name='view_queries'),
    path('upload_pyq/', views.upload_pyq, name='upload_pyq'),
    path('view_mypyqs/', views.view_mypyqs, name='view_mypyqs'),
    path('delete_mypyqs/<int:pid>/', views.delete_mypyqs, name='delete_mypyqs'),
    path('view_allpyqs/', views.view_allpyqs, name='view_allpyqs'),
    path('pending_pyqs/', views.pending_pyqs, name='pending_pyqs'),
    path('accepted_pyqs/', views.accepted_pyqs, name='accepted_pyqs'),
    path('rejected_pyqs/', views.rejected_pyqs, name='rejected_pyqs'),
    path('all_pyqs/', views.all_pyqs, name='all_pyqs'),
    path('assign_pyq_status/<int:pid>/', views.assign_pyq_status, name='assign_pyq_status'),
    path('delete_pyq/<int:pid>/', views.delete_pyq, name='delete_pyq'),
    path('viewallpyqs/', views.viewallpyqs, name='viewallpyqs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
