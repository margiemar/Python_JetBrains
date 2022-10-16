Сайт предоставляет возможность создать вакансию или резюме, сохраняя данные в SQL в виде "Автор: описание".
Стартовая страница http://localhost:8000/ даёт следующие возможности:

Welcome to HyperJob!
Login page
Logout page
Sign up page
Vacancy list
Resume list
Personal profile

Для авторизованного суперпользователя - поле для создания вакансии, для обычного пользователя - резюме.

Создание юзера и суперюзера
************************************

from django.contrib.auth.models import User


User.objects.create_superuser(
   username='admin', email='admin@example.com', password='SeCreTPaSsWorD'
)

User.objects.create_user(
   username='usual_user', email='user@example.com', password='NotSecRetAtAll'
)

или
python manage.py createsuperuser
