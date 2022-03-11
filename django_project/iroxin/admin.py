from django.contrib import admin

from .models import Subscriber, Product


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("pk",
                    "user_id",
                    "username",
                    "phone",
                    "company",
                    "status",)
    list_filter = ("status",
                   "updated_date",
                   "company",)
    list_editable = ("status",)
    search_fields = ("user_id",
                     "status",
                     "created_date",
                     "updated_date",)
    empty_value_display = "-пусто-"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Product, ProductAdmin)