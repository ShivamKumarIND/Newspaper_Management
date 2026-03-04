from django.db import models
from django.utils import timezone

NEWSPAPER_CHOICES = [
    ('Hindustan', 'Hindustan'),
    ('Dainik Jagaran', 'Dainik Jagaran'),
    ('Dainik Bhaskar', 'Dainik Bhaskar'),
    ('Prabhat Khabar', 'Prabhat Khabar'),
    ('AAJ', 'AAJ'),
    ('The Times Of India', 'The Times Of India'),
    ('The Hindu', 'The Hindu'),
    ('Hindustan Times', 'Hindustan Times'),
]

PROFIT_PER_NEWSPAPER = 1  # ₹1 per newspaper


class NewspaperSubscription(models.Model):
    newspaper = models.CharField(max_length=50, choices=NEWSPAPER_CHOICES)
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    start_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.newspaper} ({self.location})"

    class Meta:
        verbose_name = "Newspaper Subscription"
        ordering = ['-start_date']


class ClosedNewspaper(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    reason = models.TextField()
    closed_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - Closed on {self.closed_date.strftime('%d %b %Y')}"

    class Meta:
        verbose_name = "Closed Newspaper"
        ordering = ['-closed_date']


class Payment(models.Model):
    """Admin-managed model to track subscriber payment status."""
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    months_paid_till = models.DateField(help_text="Last month for which payment has been made")
    due_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.mobile}) - Paid till {self.months_paid_till.strftime('%B %Y')}"

    class Meta:
        verbose_name = "Payment Record"
        ordering = ['-last_updated']


class Complaint(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    issue = models.TextField()
    complaint_date = models.DateTimeField(default=timezone.now)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Complaint by {self.name} on {self.complaint_date.strftime('%d %b %Y')}"

    class Meta:
        verbose_name = "Complaint"
        ordering = ['-complaint_date']


class Distributor(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    registered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.mobile}"

    class Meta:
        verbose_name = "Distributor"
        ordering = ['-registered_date']


class NewspaperSoldRecord(models.Model):
    """Tracks daily newspaper sold/left data."""
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    total_received = models.PositiveIntegerField()
    newspaper_details = models.JSONField(default=dict, help_text="JSON of newspaper_type: quantity taken")
    total_taken = models.PositiveIntegerField(default=0)
    total_sold = models.PositiveIntegerField(default=0)
    total_remaining = models.PositiveIntegerField(default=0)
    net_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.date} | Sold: {self.total_sold} | Remaining: {self.total_remaining}"

    class Meta:
        verbose_name = "Newspaper Sold Record"
        ordering = ['-date']
