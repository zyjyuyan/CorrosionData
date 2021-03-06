from django.contrib import admin
from main.models import Environment, Chemical, CorrosionResult

admin.site.register(Environment)
admin.site.register(Chemical)
# admin.site.register(CorrosionResult)

@admin.register(CorrosionResult)
class CorrosionResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'starttime', 'endtime', 'corrosionrate')
    search_fields = ('starttime', 'endtime', 'corrosionrate')
    list_filter = ("id", "corrosionrate")
    date_hierarchy='modified'

# admin.site.register(CardnoteCard)
# @admin.register(CardnoteCard)
# class CardnoteCardAdmin(admin.ModelAdmin):
#     list_display = ('id', 'userid', 'user', 'title', 'kcol', 'vcol', 'category', 'created', 'modified')
#     search_fields = ('title', 'kcol', 'vcol')
#     list_filter = ('userid', 'category')
#     date_hierarchy = 'modified'


# # admin.site.register(CardnoteItem)
# @admin.register(CardnoteItem)
# class CardnoteItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cardnotecardid', 'kword', 'val', 'created', 'modified')
#     search_fields = ('kword', 'val')
#     date_hierarchy = 'modified'


# # admin.site.register(ShortUrl)
# @admin.register(ShortUrl)
# class ShortUrlAdmin(admin.ModelAdmin):
#     list_display = ('id', 'userid', 'name', 'url', 'created', 'modified')
#     search_fields = ('name', 'url')
#     list_filter = ('userid',)
#     date_hierarchy = 'modified'
