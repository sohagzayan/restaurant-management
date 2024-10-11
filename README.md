# Restaurant Management API

## Overview

This repository contains the backend API for managing restaurant operations. It includes features like user authentication, restaurant location management, menu creation, and more.

## Roadmap

### Phase 1: User Management

- Custom user model using Django's `AbstractBaseUser`.
- JWT-based authentication for login and registration.

### Phase 2: Restaurant and Menu Management

- Manage multiple restaurant locations.
- Menu creation and management for each restaurant.

### Phase 3: Orders and Payments (Future)

- Integration with payment gateways.
- Order tracking and real-time updates.

### Phase 4: Reviews and Ratings

- Users can submit reviews and ratings.
- Nested comments, likes, and dislikes functionality.

## How to Use This Repository

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/restaurant-management-api.git
   cd restaurant-management-api
   ```

2. **Set Up the Environment**
   Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure to set up your PostgreSQL database and configure the `.env` file for environment variables.

3. **Run Migrations**
   Run the following commands to set up the database:

   ```bash
   python manage.py migrate
   ```

4. **Start the Server**
   You can now start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### 1. **User Authentication**

- **Endpoint**: `/api/auth/register/`
- **Method**: POST
- **Description**: Registers a new user in the system.
- **Payload**:
  ```json
  {
    "email": "user@example.com",
    "password": "yourpassword",
    "name": "User Name"
  }
  ```
- **Response**:

  ```json
  {
    "message": "User registered successfully.",
    "token": "JWT token"
  }
  ```

- **Endpoint**: `/api/auth/login/`
- **Method**: POST
- **Description**: Logs in an existing user.
- **Payload**:
  ```json
  {
    "email": "user@example.com",
    "password": "yourpassword"
  }
  ```
- **Response**:
  ```json
  {
    "token": "JWT token"
  }
  ```

### 2. **Restaurant Management**

- **Endpoint**: `/api/restaurant/`
- **Method**: GET
- **Description**: Retrieves a list of all restaurants with optional query parameters for filtering (e.g., by location or status).
- **Query Parameters**:
  - `lat`: Latitude of the location.
  - `lng`: Longitude of the location.
  - `verified`: Boolean, filter by verified status.
- **Response**:

  ```json
  [
    {
      "id": 1,
      "name": "Restaurant Name",
      "location": "123 Main St",
      "lat": 23.7624072,
      "lng": 90.3388028,
      "verified": true
    }
  ]
  ```

- **Endpoint**: `/api/restaurant/create/`
- **Method**: POST
- **Description**: Creates a new restaurant entry.
- **Payload**:
  ```json
  {
    "name": "New Restaurant",
    "location": "123 New St",
    "lat": 23.7624072,
    "lng": 90.3388028,
    "verified": true
  }
  ```
- **Response**:
  ```json
  {
    "message": "Restaurant created successfully.",
    "restaurant": {
      "id": 1,
      "name": "New Restaurant",
      "location": "123 New St",
      "lat": 23.7624072,
      "lng": 90.3388028,
      "verified": true
    }
  }
  ```

### 3. **Menu Management**

- **Endpoint**: `/api/menu/`
- **Method**: GET
- **Description**: Retrieves the menu for a given restaurant.
- **Query Parameters**:
  - `restaurant_id`: ID of the restaurant.
- **Response**:

  ```json
  [
    {
      "id": 1,
      "name": "Dish Name",
      "price": 12.99,
      "description": "Delicious dish."
    }
  ]
  ```

- **Endpoint**: `/api/menu/create/`
- **Method**: POST
- **Description**: Adds a new menu item for a restaurant.
- **Payload**:
  ```json
  {
    "restaurant_id": 1,
    "name": "New Dish",
    "price": 15.99,
    "description": "Tasty new dish."
  }
  ```
- **Response**:
  ```json
  {
    "message": "Menu item created successfully.",
    "menu_item": {
      "id": 1,
      "name": "New Dish",
      "price": 15.99,
      "description": "Tasty new dish."
    }
  }
  ```

### 4. **Review and Rating Management**

- **Endpoint**: `/api/review/`
- **Method**: POST
- **Description**: Submit a review for a restaurant.
- **Payload**:
  ```json
  {
    "restaurant_id": 1,
    "review": "Great food!",
    "rating": 5
  }
  ```
- **Response**:
  ```json
  {
    "message": "Review submitted successfully.",
    "review": {
      "id": 1,
      "restaurant_id": 1,
      "review": "Great food!",
      "rating": 5,
      "likes": 0,
      "dislikes": 0
    }
  }
  ```

## Future Enhancements

- Order Management
- Payment Gateway Integration
- Advanced Review and Comment Systems
