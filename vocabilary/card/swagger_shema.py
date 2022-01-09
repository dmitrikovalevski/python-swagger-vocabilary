from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

schema = get_schema_view(
    title='Vocabilary',
    description='Vocabilary API'
)


class SwaggerDocumentationTemplateView(TemplateView):
    template_name = 'documentation.html'
    extra_context = {
        'schema_url': 'openapi'
    }