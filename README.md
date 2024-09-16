# Django
https://note.com/mega_gorilla/n/n256a33c01afb

https://docs.djangoproject.com/ja/5.0/intro/tutorial01/
## インストール
$ pip install django

## プロジェクト作成
$ django-admin startproject mysite

## サーバ起動
$ python manage.py runserver

## アプリケーション作成
$ python manage.py startapp polls

## Database の設定
mysite/settings.pyのINSTALLED_APPSに追加
```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

## Database の設定
$ python manage.py migrate

## フィールドの型
https://docs.djangoproject.com/ja/5.1/ref/models/fields/#field-types

