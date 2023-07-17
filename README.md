# qctrl-assignment
--


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
