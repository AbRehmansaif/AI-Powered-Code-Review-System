from django.db import models
from django.utils.translation import gettext_lazy as _
from user_code.enums import Language, Framework, Options
from user.models import User


class SelectLanguage(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name='select_language'
    )
    
    pl = models.CharField(
        max_length=10, verbose_name=_('Programming Language'),
        choices=Language.choices(), default=Language.Python
    )
    framework = models.CharField(
        max_length=10, verbose_name=_('Programming Language'),
        choices=Framework.choices(), default=Framework.Django
    )
    
class CodeReviewSelection(models.Model):
    review_type = models.CharField(
        max_length=10, verbose_name=_('Options'),
        choices=Options.choices(), default=Options.Styling
    ) 
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='code_review_selection'
    )
    
    
    
    