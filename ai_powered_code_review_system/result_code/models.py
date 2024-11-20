from django.db import models
from django.utils.translation import gettext_lazy as _
from user_code.models import CodeReviewSelection
from user_code.enums import SeverityLevel


class CodeReviewReport(models.Model):
    class Meta:
        verbose_name = _("Code Review Report")
        verbose_name_plural = _("Code Review Reports")
        
    submission = models.OneToOneField(
        CodeReviewSelection, on_delete=models.CASCADE,
        related_name="code_review_report",
        verbose_name=_("Code Submission")
    )
    
    ai_report = models.TextField(
        verbose_name=_("AI Report"),
        null=True, blank=True
    )
    
    corrected_code = models.TextField(
        verbose_name=_("Corrected Code"),
        null=True, blank=True
    )
    
    issues_found = models.TextField(
        verbose_name=_("Issues Found"),
        null=True, blank=True
    )
    
    issues_fixed = models.TextField(
        verbose_name=_("Issues Fixed"),
        null=True, blank=True
    )
    
    execution_time = models.FloatField(
        verbose_name=_("Execution Time"),
        null=True, blank=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return f"Report for {self.submission.user.username} - {self.created_at.date()}"