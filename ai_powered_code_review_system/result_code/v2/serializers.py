from rest_framework import serializers
from result_code.models import CodeReviewReport


class CodeReviewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeReviewReport
        fields = (
            'submission', 'ai_report',
            'corrected_code', 'issues_found',
            'issues_fixed', 'execution_time',
            'created_at'
        )