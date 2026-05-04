Django + HTMX
CRUD Operations & Search with Class-Based Views

Book Store

List of Stores, Books and Author

1. Create and activate a virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate

2. Install Django

pip install django

3. Create the project and app

django-admin startproject bookstore .
python manage.py startapp book

4. Register the app in settings.py

INSTALLED_APPS = [
    # ... Django built-ins ...
    'store',
]

<img width="477" height="223" alt="image" src="https://github.com/user-attachments/assets/2a258b91-3b71-4450-8d83-866a2b25004c" />

<img width="501" height="456" alt="image" src="https://github.com/user-attachments/assets/720c9530-eecf-48f4-8ead-aea400d41f02" />

<img width="533" height="434" alt="image" src="https://github.com/user-attachments/assets/721a76ae-2a6d-43a0-afd9-85efaf0e433b" />

<img width="456" height="421" alt="image" src="https://github.com/user-attachments/assets/faad1899-fce7-431f-b65a-bd91870ccdf0" />

<img width="340" height="417" alt="image" src="https://github.com/user-attachments/assets/763f4998-7a11-4b81-811a-23c522391e35" />





