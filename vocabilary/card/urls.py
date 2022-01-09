from django.urls import path
from .swagger_shema import schema, SwaggerDocumentationTemplateView

from .views import index, all_models
from .api import CardListApiView, CardCRUD

urlpatterns = [
    path('', index, name='index'),
    path('all_models/', all_models, name='cards'),
    path('openapi/', schema, name='openapi'),
    path('swagger/', SwaggerDocumentationTemplateView.as_view(), name='swagger'),
    path('card/', CardListApiView.as_view()),
    path('card/<int:pk>/', CardCRUD.as_view()),
]
