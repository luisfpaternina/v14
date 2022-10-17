# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ReportXlsx(models.AbstractModel):
    _name = 'report.generate_reports.report_customer_xlsx'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, partners):
        # reporte
        workbook.add_worksheet('reporte lfpv')
