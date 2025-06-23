from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='upload_files/') # uploads to 'documents/' directory

    def __str__(self):
        return self.name

    # deleteメソッドをオーバーライドして、実際のファイルを削除するようにした
    def delete(self):
        self.file.delete()
        super().delete()
