from django.urls import path
from . import views
urlpatterns = [
    # ここにURLパターンを追加していく
    path('', views.hello_world, name='hello'),  # 例：ルートに hello_world ビューを割り当てる
]
