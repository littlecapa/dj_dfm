from django.db import models

class Config(models.Model):
    version = models.CharField(max_length=10, default="1.0")
    start_twic_nr = models.IntegerField(default=1565)
    volume_twic = models.CharField(max_length=50, default="VOLUME_DATALAKE_MINI")
    volume_import = models.CharField(max_length=50, default="VOLUME_DATALAKE_FRITZ")
    volume_download_iccf = models.CharField(max_length=50, default="VOLUME_DATALAKE_DOWN")
    twic_folder = models.CharField(max_length=100, default="chess/twic")
    iccf_folder = models.CharField(max_length=100, default="chess/iccf")
    sub_folder_unzipped = models.CharField(max_length=50, default="pgn")
    folder_import = models.CharField(max_length=100, default="chess_import")
    base_url_twic = models.URLField(default="https://theweekinchess.com/zips/twic")
    base_url_iccf = models.URLField(default="https://gamesarchive.iccf.com/archive")
    max_missing_twic = models.IntegerField(default=1)
    sub_folder_zst = models.CharField(max_length=50, default="zst")
    user_agent = models.CharField(
        max_length=255, 
        default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
    )

    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configuration"

    def save(self, *args, **kwargs):
        # Ensure only one Config instance exists
        if not Config.objects.exists() or self.pk is not None:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Only one Config instance is allowed.")

    def __str__(self):
        return f"Configuration {self.version}"
