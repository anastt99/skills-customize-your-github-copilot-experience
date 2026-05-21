# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework to practice defining routes, validating request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description

Write a FastAPI application that exposes endpoints for managing a simple collection of items.

#### Requirements
Completed program should:

- Define a FastAPI app instance in `starter-code.py`
- Implement routes for listing items and retrieving a single item by ID
- Return JSON data with proper HTTP status codes
- Use a Pydantic model for request and response data

### 🛠️ Add Create and Update Functionality

#### Description

Extend the API so users can add new items and update existing items through POST and PUT requests.

#### Requirements
Completed program should:

- Accept new item data in the request body using a Pydantic model
- Create items with unique IDs and store them in an in-memory dictionary
- Update existing items by ID and return the updated item
- Handle missing item IDs with a `404 Not Found` error
