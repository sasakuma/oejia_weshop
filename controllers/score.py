# -*- coding: utf-8 -*-

import json

from odoo import http
from odoo.http import request

from .. import defs
from .base import BaseController

import logging

_logger = logging.getLogger(__name__)


class WxappScore(http.Controller, BaseController):

    @http.route('/<string:sub_domain>/score/send/rule', auth='public', methods=['GET', 'POST'], csrf=False)
    def list(self, sub_domain, code=5, **kwargs):
        try:
            ret, entry = self._check_domain(sub_domain)
            if ret:return ret

            data = []

            return self.res_err(700)

        except Exception as e:
            _logger.exception(e)
            return self.res_err(-1, str(e))

    @http.route('/<string:sub_domain>/shop/goods/kanjia/list', auth='public', methods=['GET', 'POST'], csrf=False)
    def kanjia_list(self, sub_domain, **kwargs):
        try:
            ret, entry = self._check_domain(sub_domain)
            if ret:return ret

            data = []

            return self.res_ok(data)

        except Exception as e:
            _logger.exception(e)
            return self.res_err(-1, str(e))

    @http.route('/<string:sub_domain>/discounts/coupons', auth='public', methods=['GET', 'POST'], csrf=False)
    def coupons(self, sub_domain, type=None, **kwargs):
        try:
            ret, entry = self._check_domain(sub_domain)
            if ret:return ret

            data = []

            return self.res_err(700)

        except Exception as e:
            _logger.exception(e)
            return self.res_err(-1, str(e))

    @http.route('/<string:sub_domain>/discounts/my', auth='public', methods=['GET', 'POST'], csrf=False)
    def my_coupons(self, sub_domain, type=None, **kwargs):
        try:
            ret, entry = self._check_domain(sub_domain)
            if ret:return ret

            data = []

            return self.res_err(700)

        except Exception as e:
            _logger.exception(e)
            return self.res_err(-1, str(e))


    @http.route('/<string:sub_domain>/shop/goods/reputation', auth='public', methods=['GET', 'POST'], csrf=False)
    def reputation(self, sub_domain, goodsId=None, **kwargs):
        try:
            ret, entry = self._check_domain(sub_domain)
            if ret:return ret

            data = []

            return self.res_ok(data)

        except Exception as e:
            _logger.exception(e)
            return self.res_err(-1, str(e))
