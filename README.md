# qctrl-assignment
Django app serving a paginated Graphql Person search service at `/graphql`

The default page size has been set to:
```
DEFAULT_PAGE_SIZE = 2
```

`db.sqlite3` has been commited with test data.

## Requirements
- docker
- docker-compose

## Build and run it in local
```text
$ docker-compose up --build
```

Navigate to `localhost:8000/graphql`

Query structure:
```text
query {
  people(page_number: Int?) {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```

## Tests
```text
$ docker-compose run app pytest personsearch/
```
