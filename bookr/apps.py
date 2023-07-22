"""This class is used to overwrite admin panel site"""
from django.contrib.admin.apps import AdminConfig

class ReviewsAdminConfig(AdminConfig):
    default_site = 'admin.BookrAdminSite'