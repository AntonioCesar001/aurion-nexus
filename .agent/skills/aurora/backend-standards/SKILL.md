# SKILL.md — Backend Architecture Standards

## Description
Standards for building scalable, secure backend services in the Aurora squad.

## When to use
Any task involving APIs, data models, business logic, or Supabase integration.

## API design

### RESTful endpoints
- Use proper HTTP methods: GET (read), POST (create), PUT/PATCH (update), DELETE (remove)
- Return correct status codes: 200, 201, 400, 401, 403, 404, 500
- Version APIs when breaking changes occur: `/api/v1/`, `/api/v2/`
- Always return structured error responses:
```json
{ "error": { "code": "VALIDATION_ERROR", "message": "Email is required" } }
```

### Input validation
- Validate ALL inputs at the API boundary
- Use schema validation (Zod, Joi, or equivalent)
- Never trust client-side validation alone

## Database standards

### Schema modeling
- Normalize to 3NF minimum
- Use UUIDs for primary keys
- Always include `created_at` and `updated_at` timestamps
- Name tables in snake_case plural: `users`, `order_items`

### Supabase specific
- Enable Row-Level Security (RLS) on all tables
- Write explicit RLS policies — never disable RLS "temporarily"
- Use Edge Functions for complex business logic
- Use database functions for computed columns

### Migrations
- Every schema change goes through a versioned migration
- Migration files must be reversible (up + down)
- Test migrations on staging before production

## Auth patterns
- Use JWT for stateless authentication
- Implement refresh token rotation
- Never store passwords in plain text
- Use Supabase Auth when available — don't reinvent

## Performance
- Index frequently queried columns
- Avoid N+1 queries (use joins or batch fetches)
- Paginate list endpoints (limit/offset or cursor)
- Cache read-heavy endpoints when appropriate

## Owner
CTO (`backend_architect`)
