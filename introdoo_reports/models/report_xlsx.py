# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging


class ReportXlsx(models.AbstractModel):
    _name = 'report.generate_reports.report_customer_xlsx'
    _inherit = 'report.report_xlsx.abstract'
