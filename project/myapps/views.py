from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
  # return HttpResponse("Hello World")
  # render関数を使ってテンプレートファイルを指定してレンダリングする
  return render(request, 'hello.html')

from .models import Memo # 作成した Memo モデルをインポート
def memo_list(request):
    """
    全てのメモを取得してテンプレートに渡すビュー
    """
    memos = Memo.objects.all().order_by('-created_at') # 全てのメモを作成日時の降順で取得
    context = {'memos': memos}                        # テンプレートに渡すデータ (辞書形式)
    return render(request, 'myapps/memo_list.html', context) # 新しいテンプレートを指定
