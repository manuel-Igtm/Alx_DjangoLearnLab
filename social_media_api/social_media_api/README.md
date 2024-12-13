# Social Media API

## Setup
1. Install dependencies: `pip install django djangorestframework djangorestframework-simplejwt`.
2. Run migrations: `python manage.py migrate`.
3. Start the server: `python manage.py runserver`.

## Features
- User registration.
- Token-based authentication.
- Profile management.

## Endpoints
- `POST /api/accounts/register/`: Register a new user.
- `GET /api/accounts/profile/`: View user profile.
- `PUT /api/accounts/profile/`: Update user profile.
