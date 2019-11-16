from django.db import models
from illusion.file_upload import file_upload_path
# from datetime import datetime


# Create your models here.



class Member_db(models.Model):
    user_num = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    join_date = models.DateTimeField(auto_created=True, auto_now=True)
    profile = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.user_id


class History_db(models.Model):
    history_num = models.AutoField(primary_key=True)  # history_db의 프라이머리키가 history_num이다! 라는 것을 지정해줘야한다.
    user_num = models.ForeignKey(Member_db, on_delete=models.CASCADE)
    history_image_name = models.CharField(max_length=45)
    history_date = models.DateTimeField(auto_created=True, auto_now=True)
    style_name = models.CharField(max_length=45)
    history_location = models.CharField(max_length=45)

    def __str__(self):
        return self.history_image_name


class Timeline_db(models.Model):
    time_num = models.AutoField(primary_key=True)
    user_num = models.ForeignKey(Member_db, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_created=True, auto_now=True)
    time_image_name = models.CharField(max_length=45)
    time_comment = models.CharField(max_length=45)
    time_location = models.CharField(max_length=45)

    def __str__(self):
        return self.time_image_name


class Reply_db(models.Model):
    reply_num = models.AutoField(primary_key=True)
    time_num = models.ForeignKey(Timeline_db, on_delete=models.CASCADE)
    user_num = models.ForeignKey(Member_db, on_delete=models.CASCADE)
    reply_comment = models.CharField(max_length=45)
    reply_time = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.reply_comment


class Style_db(models.Model):
    style_num = models.AutoField(primary_key=True)
    style_name = models.CharField(max_length=45)
    style_path = models.CharField(max_length=45)

    def __str__(self):
        return self.style_name


class ContentImage(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.FileField(upload_to=file_upload_path, null=True)


class Preview(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.FileField(upload_to=file_upload_path, null=True)
    style_id = models.CharField(max_length=45)
    url = models.CharField(max_length=1000)





from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUser(AbstractBaseUser):
    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    objects = BaseUserManager()

    uid = models.CharField(
        primary_key=True,
        unique=True,
        max_length=100,
        verbose_name='유저 UID (Firebase 에서 자동 생성)'
    )
    last_login = models.DateTimeField(auto_now=True, verbose_name='최근 로그인 일자')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')

    USERNAME_FIELD = 'uid'

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_active

    def has_module_perms(self, app_label):
        return self.is_active


# from django.contrib.auth.models import User
# from django.db import models
# from django.db.models.signals import post_save
#
#
# class Post(TimeStampedModel):
#     title = models.CharField(max_length=512)
#     content = models.TextField()
#     author = models.ForeignKey(User)
#
#     def get_subscribers(self):
#         users = User.objects.all()
#         users = users.exclude(pk=self.author.pk)
#         return users
