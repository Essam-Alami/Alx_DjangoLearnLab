from django.urls import path
from .views import NotificationListView, NotificationMarkReadView, mark_all_read

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications-list'),
    path('<int:pk>/mark-read/', NotificationMarkReadView.as_view(), name='notification-mark-read'),
    path('mark-all-read/', mark_all_read, name='notifications-mark-all-read'),
]
