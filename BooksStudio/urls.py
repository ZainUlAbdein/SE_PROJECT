from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]


admin.site.site_header = "Book Studio"
admin.site.site_title = "Book Studio superadmin"
admin.site.index_title = "Welcome to superadmin portal"
