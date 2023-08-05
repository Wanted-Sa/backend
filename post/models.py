from django.db import models


class Post(models.Model):
    title = models.CharField("제목", max_length=255)
    content = models.TextField("내용")
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    is_deleted = models.BooleanField("삭제 여부", default=False)
    account = models.ForeignKey("account.Account", verbose_name="작성자", on_delete=models.PROTECT)

    def __str__(self):
        return f"[{self.id}][{self.title}]"

    class Meta:
        db_table = "POST"