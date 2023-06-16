from django.db import models

# Create your models here.
class Menu(models.Model):
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
    
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    font_awesome_icon = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class SubMenu(models.Model):
    class Meta:
        verbose_name = 'Sub Menu'
        verbose_name_plural = 'Sub Menus'
    
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    font_awesome_icon = models.CharField(max_length=2048)
    parent_menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, null=False, blank=False)
    new_tab = models.BooleanField(default=False)

    def __str__(self):
        return self.text