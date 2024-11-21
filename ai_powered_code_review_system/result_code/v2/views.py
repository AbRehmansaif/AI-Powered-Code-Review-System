from rest_framework import viewsets, permissions
from result_code.v2.serializers import CodeReviewReportSerializer
from result_code.models import CodeReviewReport


class CodeReiewViewSet(viewsets.ModelViewSet):
    queryset = CodeReviewReport.objects.all()
    serializer_class = CodeReviewReportSerializer
    permission_class = [permissions.AllowAny]
    http_method_names = ['get']