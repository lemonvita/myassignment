from typing import Any

from django.core.paginator import Paginator
from graphql import GraphQLResolveInfo

from .models import Person

# Set default page size here
DEFAULT_PAGE_SIZE = 2


def list_people(obj: Any, info: GraphQLResolveInfo, page_number=1):
    people_list = Person.objects.order_by('name')
    page = Paginator(people_list, DEFAULT_PAGE_SIZE).page(page_number)
    return [
        {
            'name': person.name,
            'email': person.email,
            'address': person.address
        }
        for person in page.object_list
    ]
