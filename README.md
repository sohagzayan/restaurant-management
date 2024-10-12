# Restaurant Management API

## Overview

This repository contains the backend API for managing restaurant operations. It includes features like user authentication, restaurant location management, menu creation, and more.

## How to Use This Repository

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sohagzayan/restaurant-management.git
   cd restaurant-management
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

**Register New user (POST)**

```bash
  /api/auth/register/
```

**Get all user list (GET)**

```bash
  /api/auth/userlist/
```

**User login (POST)**

```bash
  /api/auth/login/
```

**Change user password with old password (PUT)**

```bash
  /api/auth/change_password/
```

**Logout user with invalid refresh token (POST)**

```bash
  /api/auth/logout/
```

## Restaurant

**Create new restaurant (POST)**

```bash
  /api/restaurants-create/
```

**Get all restaurant (GET)**

```bash
  /api/restaurants-list/
```

**Create location (POST)**

```bash
  /api/restaurants/1/locations-create/
```

**Create menu (POST)**

```bash
  /api/locations/1/menus-create/
```

**Get menu list (GET)**

```bash
/api/locations/1/menus-list/
```

**Create categories (POST)**

```bash
  /api/menus/1/categories-create/
```

**Get categories list (GET)**

```bash
  /api/menus/1/categories-list/
```

**Create item (POST)**

```bash
  /api/categories/1/items-create/
```

**Get item list (GET)**

```bash
 /api/categories/1/items-list/
```
