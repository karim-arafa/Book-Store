from django.contrib import admin
from .models import Store, Category, Tag,Isbn
from .forms import StoreForm, CatForm


# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    form = StoreForm
    list_display = ("title", "author","isbn")
    list_filter = ("categories",)
    search_fields = ("title",)


class StoreInline(admin.StackedInline):
    model = Store
    max_num = 3
    extra = 1


class TagAdmin(admin.ModelAdmin):
    inlines = [StoreInline]


class CategoryAdmin(admin.ModelAdmin):
    form = CatForm


admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Isbn)
admin.site.register(Tag, TagAdmin)
