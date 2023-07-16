from ariadne import QueryType, make_executable_schema, load_schema_from_path
from .models import Person

from config.settings import BASE_DIR

person_type_defs = load_schema_from_path(
    BASE_DIR / "app" / "schema" / "people.graphql"
)
query = QueryType()


def list_people(*_):
    return [
        {
            "name": person.name,
            "email": person.email,
            "address": person.address
         }
        for person in Person.objects.all()
    ]


query.set_field("people", list_people)

schema = make_executable_schema(person_type_defs, query)
