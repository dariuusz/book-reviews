from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book,
        BookContributor, Review)

class BookAdmin(admin.ModelAdmin):
    """Return filters on the Book-Admin page by publishers
    and by years and months. Also, adding a search bar for title, isbn
    and ForeignKeyField."""
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')

    def isbn13(self, obj):
        """Return representation of ISBN number as:
        '9780316769174' --> '978-0-31-676917-4'"""
        return "{}-{}-{}-{}-{}".format\
                                (obj.isbn[0:3], obj.isbn[3:4],\
                                 obj.isbn[4:6], obj.isbn[6:11],\
                                 obj.isbn[12:13])

class ContributorAdmin(admin.ModelAdmin):
    """Return filters on the Contributor-Admin page."""
    list_display = ('first_names', 'last_names','initialled_name')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')

class ReviewAdmin(admin.ModelAdmin):
    """Return fields excluding date_edited on Admin page."""
    date_hierarchy = 'date_created'
    list_display = ('creator', 'rating')
    exclude = ('date_edited', 'creator', 'rating')
    list_filter = ('date_created',)
    search_fields = ('creator',)

class PublisherAdmin(admin.ModelAdmin):
    """Return filters for Publisher-Admin page."""
    list_display = ('name', 'email')
    list_filter = ('name',)
    search_fields = ('name',)

class BookContributorAdmin(admin.ModelAdmin):
    """Return filters for BookCOntributor-Admin page."""
    list_display = ('book', 'role')

# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
admin.site.register(Review, ReviewAdmin)