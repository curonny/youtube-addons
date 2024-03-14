# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
import json
from datetime import datetime

from odoo import api, fields, models, _


class ExcelReportWizard(models.TransientModel):
    _name = 'excel.report.wizard'
    _description = "Excel report"

    date_selection = fields.Date(string="Date",
                                 default=fields.Date.context_today)

    def print_excel_report(self):
        report_obj = self.env.ref('excel_sale_product.excel_report_all')
        report_obj.name = f"Excel report [{self.date_selection}]"
        return report_obj.report_action(self, data={"date": self.date_selection})
