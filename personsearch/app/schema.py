from ariadne import QueryType, make_executable_schema, load_schema_from_path
from config.settings import BASE_DIR

from .resolver import list_people

person_type_defs = load_schema_from_path(f'{BASE_DIR}/app/schema/people.graphql')
query = QueryType()
query.set_field('people', list_people)

schema = make_executable_schema(person_type_defs, query)
