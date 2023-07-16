from django.urls import path
from .schema import schema
from ariadne_django.views import GraphQLView

urlpatterns = [
    path("graphql/", GraphQLView.as_view(schema=schema), name='graphql'),
]