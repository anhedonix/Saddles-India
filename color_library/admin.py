from django.contrib import admin
from .models import Color, Category, Tag

admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Tag)

# 
# class ColorAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': ('label', 'category', 'tags', 'description')
#         }),
#         (None, {
#             'fields': ('col_l', 'col_a','col_b', 'col_c', 'col_h')
#         }),
#
#     )
#
# admin.site.unregister(Color)
# admin.site.register(Color, ColorAdmin)
