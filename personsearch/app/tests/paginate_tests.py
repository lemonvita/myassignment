import pytest as pytest
from app.models import Person, Address, State
from app.resolver import list_people


@pytest.fixture
def mock_people_list(mocker):
    people = [
        Person(name="Person1", email="p1@test.com",
               address=Address(number=1, street="Foo St", city="Foo City", state=State.NSW)),
        Person(name="Person2", email="p2@test.com",
               address=Address(number=1, street="Bar St", city="Bar City", state=State.NSW)),
        Person(name="Person3", email="p3@test.com",
               address=Address(number=1, street="Baz St", city="Baz City", state=State.NSW)),
    ]
    mocker.patch("app.models.Person.objects.all", return_value=people)
    return people


class MockGraphQLResolveInfo:
    def __init__(self):
        self.field_name = "people"


def test_list_people_page_number_supplied(mock_people_list):
    result = list_people(None, MockGraphQLResolveInfo(), page_number=2)

    assert len(result) == 1
    assert result[0]["name"] == "Person3"


def test_list_people_no_page_number(mock_people_list):
    result = list_people(None, MockGraphQLResolveInfo())

    assert len(result) == 2
    assert result[0]["name"] == "Person1"
    assert result[1]["name"] == "Person2"
