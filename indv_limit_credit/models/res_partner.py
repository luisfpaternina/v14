# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    has_credit = fields.Boolean(
        string="Has a current credit",
        compute="compute_has_a_credit")
    credit_value = fields.Float(
        string="Credit value",
        compute="compute_has_a_credit")


    def compute_has_a_credit(self):
        credit_obj = self.env['credit.limit'].search([('partner_id', '=', self.id), ('state', '=', 'approved')], limit=1)
        if credit_obj:
            self.has_credit = True
            self.credit_value = credit_obj.credit_amount
        else:
            self.has_credit = False
            self.credit_value = 0
