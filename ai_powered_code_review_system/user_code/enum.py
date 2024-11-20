from django.utils.translation import gettext_lazy as _

class Language():
    label: str
    
    PY     = "PY", _("Python")
    Java   = "JAVA", _("Java")
    JS     = "JS", _("JavaScript")
    C      = "C", _("C")
    Cpp    = "CPP", _("C++")
    Csharp = "C#", _("C#")
    PHP    = "PHP", _("PHP")
    
class Framework():
    label: str
    
    REACT   = "REACT", _("React")
    ANGULAR = "ANGULAR", _("Angular")
    VUE     = "VUE", _("Vue")
    SPRING  = "SPRING", _("Spring")
    Django  = "DJANGO", _("Django")
    
class Options():
    label: str
    
    Security = "SECURITY", _("Security")
    Effiency = "EFFIENCY", _("Efficiency")
    Styling  = "STYLING", _("Styling")