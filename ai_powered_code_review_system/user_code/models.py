from django.db import models
from django.utils.translation import gettext_lazy as _
from user_code.enums import Language, Framework, Options, StatusOptions
from user.models import User


class SelectLanguage(models.Model):
    class Meta:
        verbose_name = _('Select Language')
        verbose_name_plural = _('Select Languages')
        
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name='select_language', verbose_name=_('User')
    )
    
    pl = models.CharField(
        max_length=10, verbose_name=_('Programming Language'),
        choices=Language.choices, default=Language.PY
    )
    
    framework = models.CharField(
        max_length=10, verbose_name=_('Programming Language'),
        choices=Framework.choices, default=Framework.Django
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return f"{self.user.username} - {self.get_pl_display()}"
    
class CodeReviewSelection(models.Model):
    class Meta:
        verbose_name = _("Code Review Selection")
        verbose_name_plural = _("Code Review Selections")
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='code_review_selection',
        verbose_name=_('User')
    )
    
    review_type = models.CharField(
        max_length=10, verbose_name=_('Review Type'),   
        choices=Options.choices, default=Options.Styling
    ) 
    
    language = models.ForeignKey(
        SelectLanguage, on_delete=models.CASCADE,
        related_name='code_review_language_selection',
        verbose_name=_('Language Selection')
    )
    
    code_content = models.TextField(
        verbose_name=_('Code Content')
    )
    
    submitted_at = models.DateTimeField(
        auto_now_add=True
    )
    
    status = models.CharField(
        max_length=10, verbose_name=_('Status'),
        choices=StatusOptions.choices, default=StatusOptions.Processing
    )
    
    def __str__(self):
        return f"{self.user.username} - {self.get_review_type_display()}"
    
    