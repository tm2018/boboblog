# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from random import choice
import os,shutil




# 用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,所以修改str类的title方法就可以实现.
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


# Create your models here.

class VmaigUser(AbstractUser):
    #注册时从路径中随机选择一个图片作为头像
    def select_pic():
            base_dir = os.getcwd()
            pic_dir = base_dir+'/vmaig_auth/static/tx/'
            dirs_files = os.listdir(pic_dir)
            pic = choice(dirs_files)
            user_tx = '/static/tx/'+pic
            print user_tx
            return user_tx
    img = models.CharField(max_length=200, default=select_pic(),
                           verbose_name=u'头像地址')
    intro = models.CharField(max_length=200, blank=True, null=True,
                             verbose_name=u'简介')

    class Meta(AbstractUser.Meta):
        app_label = string_with_title('vmaig_auth', u"用户管理")
