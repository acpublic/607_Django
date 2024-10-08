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

## マイグレーション用のファイルを作成
python manage.py makemigrations polls

## フィールドの型
https://docs.djangoproject.com/ja/5.1/ref/models/fields/#field-types

## マイグレーション
$ python manage.py sqlmigrate polls 0001

## SQLコマンド作成
python manage.py sqlmigrate polls 0001

## プロジェクトに何か問題がないか確認
$ python manage.py check

## 管理サイト
http://127.0.0.1:8000/admin/ 

## 管理ユーザーを作成
$ python manage.py createsuperuser

## 管理ページ表示
```python
class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

## 管理サイトに表示
polls/admin.py
```python
from .models import Question

admin.site.register(Question)
```

