from django.db import models


class cards(models.Model):
    title = models.CharField('Название',max_length=200)
    photo = models.ImageField('Фото', upload_to='pictures')
    audio = models.FileField('Аудио', upload_to='media/audio',null=False)
    link = models.CharField('Ссылка',max_length=250)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'