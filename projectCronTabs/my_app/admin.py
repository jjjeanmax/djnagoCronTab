from django.contrib import admin
from .models import Test, Document


@admin.register(Test)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(Document)
class AdminDocument(admin.ModelAdmin):
    list_display = (
        "upload_file",
        "expiration_date",
        "create_at",
        "updated_at",
        "expired")
