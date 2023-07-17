from typing import Any

from django.core.paginator import Paginator
from graphql import GraphQLResolveInfo

from .models import Person

# Set default page size here
default_page_size = 2


def list_people(obj: Any, info: GraphQLResolveInfo, page_number=1):
    people_list = Person.objects.all()
    page = Paginator(people_list, default_page_size).page(page_number)
    return [
        {
            "name": person.name,
            "email": person.email,
            "address": person.address
        }
        for person in page.object_list
    ]
