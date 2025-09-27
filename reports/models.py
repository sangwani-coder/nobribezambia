from django.db import models

class BribeReport(models.Model):
    MINISTRY_CHOICES = [
        ('private', 'Private Sector'),
        ('education', 'Ministry of Education'),
        ('health', 'Ministry of Health'),
        ('finance', 'Ministry of Finance and National Planning'),
        ('agriculture', 'Ministry of Agriculture'),
        ('justice', 'Ministry of Justice'),
        ('defence', 'Ministry of Defence'),
        ('home_affairs', 'Ministry of Home Affairs'),
        ('tourism', 'Ministry of Tourism'),
        ('energy', 'Ministry of Energy'),
        ('infrastructure', 'Ministry of Infrastructure and Housing'),
        ('labour', 'Ministry of Labour and Social Security'),
        ('mines', 'Ministry of Mines and Minerals Development'),
        ('transport', 'Ministry of Transport and Logistics'),
        ('youth', 'Ministry of Youth, Sport and Arts'),
        ('lands', 'Ministry of Lands and Natural Resources'),
        ('local_gov', 'Ministry of Local Government and Rural Development'),
        ('technology', 'Ministry of Technology and Science'),
        ('commerce', 'Ministry of Commerce, Trade and Industry'),
        ('unknown', 'Not Sure'),
    ]

    ministry = models.CharField(max_length=100, choices=MINISTRY_CHOICES)
    institution = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)  # was bribe_type
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    reporter_name = models.CharField(max_length=100, blank=True, null=True)
    reporter_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.institution} - {self.reason} ({self.reported_at.date()})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} from {self.name}"
