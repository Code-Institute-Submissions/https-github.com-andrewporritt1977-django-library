"""library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from library_app import urls as library_urls
from library_books import urls as book_urls
from library_books.views import all_books
from fees import urls as fees_urls
from search import urls as urls_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_books, name='index'),
    path('library/', include (library_urls)),
    path('search/', include (urls_search)),
    path('books/', include(book_urls)),
    path('fees/', include(fees_urls))
]
