# Advanced Features and Security

## Permissions and Groups
In this project, we implemented custom permissions for the `Book` model:
- `can_view`: Allows users to view the list of books.
- `can_create`: Allows users to add new books.
- `can_edit`: Allows users to modify book details.
- `can_delete`: Allows users to remove books.

### Groups:
1. **Editors**: Assigned `can_create` and `can_edit` permissions.
2. **Viewers**: Assigned `can_view` permission.
3. **Admins**: Assigned all permissions.

## Security Best Practices
- Configured Browser XSS Filter, Content Type Nosniff, and X-Frame Options.
- Enforced HTTPS using `SECURE_SSL_REDIRECT` and HSTS settings.
- Secured cookies with `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`.