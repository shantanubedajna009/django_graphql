from django.conf.urls import url
from graphene_django.views import GraphQLView
from .schema import schema

app_name = 'quiz'

urlpatterns = [
    url("^graphql/$", GraphQLView.as_view(graphiql=True, schema=schema)),
]