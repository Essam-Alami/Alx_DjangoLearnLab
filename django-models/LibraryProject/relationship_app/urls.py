from django.urls import path, include
from .views import list_books, LibraryDetailView
from .views import CustomLoginView, CustomLogoutView, register
from django.contrib import admin

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]