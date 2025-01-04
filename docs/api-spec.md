# API 規範文檔

## Overview
This document provides the API specifications for the posture capture application.

## Endpoints

### GET /
- Description: Returns a welcome message.
- Response: `{ "message": "Hello, World!" }`

### POST /users
- Description: Create a new user.
- Request Body: `{ "name": "string", "email": "string" }`
- Response: `{ "id": "integer", "name": "string", "email": "string" }`

### GET /users/{id}
- Description: Retrieve a user by ID.
- Response: `{ "id": "integer", "name": "string", "email": "string" }`

### POST /posts
- Description: Create a new post.
- Request Body: `{ "user_id": "integer", "content": "string" }`
- Response: `{ "id": "integer", "user_id": "integer", "content": "string" }`

### GET /posts/{id}
- Description: Retrieve a post by ID.
- Response: `{ "id": "integer", "user_id": "integer", "content": "string" }`
