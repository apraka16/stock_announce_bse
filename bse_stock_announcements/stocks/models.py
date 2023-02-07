from django.db import models

# Create your models here.
class Stock(models.Model):
    # SCRIP ID
    scrip_id = models.IntegerField()
    # SCRIPT_LONGNAME
    scrip_long_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.scrip_id} {self.scrip_long_name}"


class Announcement(models.Model):
    # SCRIP ID - FK
    scrip = models.ForeignKey(Stock, on_delete=models.CASCADE)
    # TIMESTAMP
    timestamp = models.DateTimeField()
    # NEWS_ID
    bse_news_id = models.CharField(max_length=200)
    # NEWSSTUB
    news_stub = models.TextField() 
    news_headline = models.TextField()

    def __str__(self) -> str:
        return f"{self.scrip.scrip_id} {self.news_stub}"
