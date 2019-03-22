from django.contrib import admin

# Register your models here.
try:
  User.objects.get(username=username)
  data = {'code': '-7', 'info': u'用户已存在'}
except User.DoesNotExist:
  user = User.objects.create_user(username, email, password)
  if user is not None:
    user.is_active = False
    user.save()