# Security Implementation and Permissions Guide

## Custom User Model
We implemented a `CustomUser` model inheriting from `AbstractUser` to include `date_of_birth` and `profile_photo`. A `CustomUserManager` handles regular and superuser creation.

## Role-Based Access Control (RBAC)
- **Groups:** Editors, Viewers, Admins.
- **Permissions:** Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) were added to the `Book` model.
- **Enforcement:** Used `@permission_required` decorators in `views.py`.

## Security Measures
1. **CSRF Protection:** All forms use `{% csrf_token %}`.
2. **SQL Injection:** Used Django ORM's parameterized queries to avoid raw SQL risks.
3. **Secure Headers:** Configured `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`, and `SECURE_BROWSER_XSS_FILTER`.
4. **HTTPS:** Enforced SSL redirects and HSTS for secure communication.