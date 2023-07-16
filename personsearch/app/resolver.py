from .models import Person


def list_people(*_):
    return [
        {
            "name": person.name,
            "email": person.email,
            "address": person.address
         }
        for person in Person.objects.all()
    ]