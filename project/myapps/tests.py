from django.test import TestCase
from .models import Memo
from django.utils import timezone

class MemoModelTest(TestCase):
    def test_create_memo(self):
        memo = Memo.objects.create(
            title="テストタイトル",
            body="テスト本文"
        )
        self.assertEqual(memo.title, "テストタイトル")
        self.assertEqual(memo.body, "テスト本文")
        self.assertIsNotNone(memo.created_at)
        self.assertIsInstance(memo.created_at, type(timezone.now()))

    def test_str_method(self):
        memo = Memo(title="タイトル", body="本文")
        self.assertEqual(str(memo), "タイトル")
