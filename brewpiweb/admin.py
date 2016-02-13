from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.translation import ugettext as _

class BrewPiAdminSite(AdminSite):
    site_header = _("BrewPi Webservice Administration")

admin_site = BrewPiAdminSite(name='brewpi-admin')

# Auth
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
