from django.contrib import admin

from catalogue.models import Author
from catalogue.models import Book
from catalogue.models import BookCopy
from catalogue.models import Genre
from catalogue.models import Language


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(Genre)
admin.site.register(Language)