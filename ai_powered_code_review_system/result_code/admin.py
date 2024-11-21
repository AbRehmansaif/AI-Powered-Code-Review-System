from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from result_code.models import CodeReviewReport


@admin.register(CodeReviewReport)
class CodeReviewReportAdmin(admin.ModelAdmin):
    
    list_display = (
        'submission', 'ai_report',
        'corrected_code', 'issues_found',
        'issues_fixed', 'execution_time',
        'created_at'
    )
    
    search_fields = [
        'submission'
    ]