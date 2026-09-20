# pretty.gay

Django application running with Docker Compose.

## Start the app

Make sure `.env` contains the required Django, PostgreSQL, and Redis settings, then run:

```powershell
docker compose up -d
```

Open the app at http://127.0.0.1:8001/

## Apply code updates

After changing Python, templates, CSS, JavaScript, or dependencies, rebuild and restart the web service:

```powershell
docker compose up -d --build web
```

## Useful commands

Check service status:

```powershell
docker compose ps
```

View web logs:

```powershell
docker compose logs -f web
```

Run Django checks:

```powershell
docker compose exec web python manage.py check
```

Run migrations:

```powershell
docker compose exec web python manage.py migrate
```

Stop the services:

```powershell
docker compose down
```
