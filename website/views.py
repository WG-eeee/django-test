from typing import Any
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name='index.html'
    def get_context_data(self):
        ctxt=super().get_context_data()
        ctxt['username']=''
        return ctxt
class AboutView(TemplateView):
    template_name='about.html'
    def get_context_data(self):
        ctxt=super().get_context_data()
        ctxt['num_services']=0
        ctxt['skills']=[
            'python',
            'c++',
        ]
        return ctxt
    
