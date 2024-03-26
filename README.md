# Simple 10 minute mail bot

## Setup:
### Env
- rename .env_example to .env and set your values.
#### Docker Env
- `TOKEN` = `your token`
- `REDIS_HOST` = `cache` dont change this value
- `REDIS_PORT` = `6379` dont change this value
- `REDIS_URL` = `redis://{REDIS_HOST}:{REDIS_PORT}` dont change this value
#### Local Env
- `TOKEN` = `your token`
- `REDIS_HOST` = `your host`
- `REDIS_PORT` = `your port`
- `REDIS_URL` = `redis://{REDIS_HOST}:{REDIS_PORT}` dont change this value
### Docker:
- docker compose up


## TODO:

- [ ] API Client

- [ ] BOT

- [ ] Tests

- [x] Add docker support
