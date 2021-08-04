from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', start_page, name='start_page'),
    path('form-url/', form_view, name='form-view'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('registration/', registration, name='registration'),
    path('registration/change_password', change_password, name='change_password'),
    path('get_comment/', get_comment, name='get_comment'),
    path('articles/', articles, name='articles'),
    path('articles/archive/', archive_article, name='archive_article'),
    path('users/', users, name='users'),
    path('articles/<int:article_number>/', article_num, name='article_num'),
    path('articles/<int:article_number>/archive/', article_num_archive, name='article_archive'),
    path('articles/<int:article_number>/<slug:slug_text>', article_num_slug, name='article_num'),
    path('users/<int:user_number>', users_num, name='users_number'),
    re_path(r'(?P<phone>(?:(?:\+?3?8?(0\d{9})$)))', verification_number, name='verification_number'),
    re_path(r'(?P<symb>[1-9a-f]{4}-[a-zA-Z0-9]{6})', symbols, name='symb'),
]

