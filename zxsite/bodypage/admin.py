from django.contrib import admin
from bodypage.models import Article,Bloger,Comment,Subcomment,Tag

admin.site.register(Article)
admin.site.register(Bloger)
admin.site.register(Comment)
admin.site.register(Subcomment)
admin.site.register(Tag)

# Register your models here.
