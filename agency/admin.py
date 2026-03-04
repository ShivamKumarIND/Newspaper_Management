from django.contrib import admin
from .models import (
    NewspaperSubscription, ClosedNewspaper, Payment,
    Complaint, Distributor, NewspaperSoldRecord
)


@admin.register(NewspaperSubscription)
class NewspaperSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'newspaper', 'location', 'start_date', 'is_active')
    list_filter = ('newspaper', 'is_active')
    search_fields = ('name', 'mobile', 'location')
    list_editable = ('is_active',)


@admin.register(ClosedNewspaper)
class ClosedNewspaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'address', 'closed_date')
    search_fields = ('name', 'mobile')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'months_paid_till', 'due_amount', 'last_updated')
    search_fields = ('name', 'mobile')
    list_editable = ('months_paid_till', 'due_amount')


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'complaint_date', 'is_resolved')
    list_filter = ('is_resolved',)
    search_fields = ('name', 'mobile')
    list_editable = ('is_resolved',)


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'age', 'registered_date')
    search_fields = ('name', 'mobile')


@admin.register(NewspaperSoldRecord)
class NewspaperSoldRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'date', 'total_received', 'total_sold', 'total_remaining', 'net_profit')
    list_filter = ('date',)
    search_fields = ('name', 'mobile')
