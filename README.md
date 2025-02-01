# My Blog - A Django & MongoDB Blog Application

## Overview

This is a personal blogging web application built with Django and MongoDB. Users can register, log in, create blog posts, and view other posts.

## Features

- User Registration & Authentication
- Create, Read, Update, and Delete (CRUD) Blog Posts
- MongoDB Integration using Djongo & MongoEngine
- Bootstrap for Responsive UI

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/myblog.git
cd myblog
```

### 2. Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install & Start MongoDB

Ensure MongoDB is installed and running:

```bash
mongod
```

### 5. Configure Database

Update `settings.py` to use MongoDB:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'myblog',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017
        }
    }
}
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure

```
myblog/
│── blog/              # Blog application
│   ├── templates/     # HTML templates
│   ├── models.py      # MongoDB models
│   ├── views.py       # Views for handling requests
│── myblog/            # Django project settings
│── static/            # Static files (CSS, JS, Images)
│── manage.py          # Django command-line tool
│── requirements.txt   # Python dependencies
```

## API Routes

| Route              | Method   | Description                    |
| ------------------ | -------- | ------------------------------ |
| `/`                | GET      | Home page displaying all posts |
| `/post/<post_id>/` | GET      | View a single blog post        |
| `/create/`         | GET/POST | Create a new blog post         |
| `/register/`       | GET/POST | User registration              |
| `/login/`          | GET/POST | User login                     |
| `/logout/`         | GET      | Logout user                    |

## Future Improvements

- Comment system
- User profile pages
- Post categories & tags

## Contributing

Feel free to fork this repo and submit a pull request with improvements.

## License

This project is licensed under the MIT License.

---

Developed with ❤️ using Django & MongoDB

