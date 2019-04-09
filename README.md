# Tùy chỉnh Model Manager trong Django 

<a target="_blank" href="https://www.djangobat.com/blog/tuy-chinh-model-manager-trong-django/"><img src="https://www.djangobat.com/media/posts/2019/04/09/model.jpg" alt="" /></a>


## BLOG djangobat

[https://www.djangobat.com/](https://www.djangobat.com/)

## setting

Đầu tiên, tải repository về máy tính:

```bash
$ git clone 
```

Cài đặt requirements:

```bash
$ cd custom_model_manager
$ pip install -r requirements.txt
```

Tạo database:

```bash
$ python manage.py migrate
```
Chạy development server

```bash
$ python manage.py runserver
```

## USE

###  Tùy chỉnh manager mặc định

```bash
$ python manage.py shell
>>> from blog.models import Post
>>> Post.public.all()
>>> Post.public.filter(title="Hoc Django")

```

### Thêm phương thức manager

```bash
$ python manage.py shell
>>> Post.public.title_count('django')
>>> Post.public.title_count('model')

```





