import xadmin
from xadmin import views
from account.models import Shop


class BaseStyleSettings:
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    site_title = 'xxx后台管理系统'
    site_footer = '武汉前锋互联网有限公司'
    menu_style = 'accordion'

xadmin.site.register(views.CommAdminView, GlobalSettings)

class ShopAdmin:
    list_display = ['shop_id', 'name', 'price', 'title']

xadmin.site.register(Shop, ShopAdmin)

