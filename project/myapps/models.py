from django.db import models

# Create your models here.
from django.utils import timezone # 作成日時用にインポート

class Memo(models.Model):
    """
    簡単なメモを保存するモデル
    """
    title = models.CharField(max_length=100) # タイトル (文字列, 最大100文字)
    body = models.TextField()                 # 本文 (長いテキスト)
    created_at = models.DateTimeField(default=timezone.now) # 作成日時 (現在時刻をデフォルトに)

    class Meta:
        db_table = 'app_memo'

    def __str__(self):
        # Django管理画面などで表示される際の文字列 representation
        return self.title
