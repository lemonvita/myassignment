from django.urls import path
from app.schema import schema
from ariadne_django.views import GraphQLView

urlpatterns = [
    path("graphql/", GraphQLView.as_view(schema=schema), name='graphql'),
]