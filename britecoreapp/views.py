from django.shortcuts import get_object_or_404, render

from .models import RiskType

def risktype(request, risktype_name):
    rt = get_object_or_404(RiskType, name=risktype_name)
    return render(request, 'risktype/index.html', {'risk_type': rt})
