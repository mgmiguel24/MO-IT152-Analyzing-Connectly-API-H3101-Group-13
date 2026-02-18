# connectly_project/urls.py
# -------------------------------------------------------
# WHAT IS THIS FILE?
# This is the MAIN ENTRANCE of your entire project's URLs.
# Every request that comes in starts here.
#
# Think of it like a building's reception desk:
#   "If you're looking for /admin/  → go to the admin area"
#   "If you're looking for /api/    → go to our API"
# -------------------------------------------------------

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The Django admin panel — a built-in web UI to manage your data
    # Visit: http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # All our API endpoints — handled by connectly_api/urls.py
    # Visit: http://127.0.0.1:8000/api/
    # This means any URL starting with /api/ gets passed to connectly_api's urls.py
    path('api/', include('connectly_api.urls')),
]
