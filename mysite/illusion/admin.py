from django.contrib import admin

from .models import History_db, Member_db, Style_db, Reply_db, Timeline_db, ContentImage, MyUser
# Register your models here.

admin.site.register(History_db)
admin.site.register(Member_db)
admin.site.register(Style_db)
admin.site.register(Reply_db)
admin.site.register(Timeline_db)
admin.site.register(ContentImage)
admin.site.register(MyUser)
