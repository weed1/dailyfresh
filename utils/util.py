# _*_ coding:utf-8 _*_

from django.contrib.auth.decorators import login_required
from django.views.generic import View


class LoginRequiredMixin(View):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
