# -*- coding: utf-8 -*-

from odoo import models, tools, _
from odoo.exceptions import ValidationError


class ExcelReport(models.AbstractModel):
    _name = 'report.excel_sale_product.excel_sale_report_product'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Excel report'

    def get_report_data(self, date_selection):
        # Get sales by date
        data = []
        move_lines = self.env['account.move.line'].search([('move_id.invoice_date', '=', date_selection)])
        [data.append({
            'partner': line.move_id.partner_id.name,
            'product': line.product_id.name,
            'price': line.price_unit,
            'standard_price': line.product_id.standard_price,
        }) for line in move_lines]
        return data

    def draw_header(self, worksheet, workbook):
        color_header_format = workbook.add_format(
            {'align': 'center', 'font_color': 'black', 'font_name': 'Courier New',
             'font_size': 10})
        worksheet.write(0, 0, "PARTNER", color_header_format)
        worksheet.write(0, 1, "PRODUCT", color_header_format)
        worksheet.write(0, 2, "PRICE", color_header_format)
        worksheet.write(0, 3, "STANDARD PRICE", color_header_format)

    def zip_from_partner(self, partner_id):
        return self.env['res.partner'].browse(partner_id).city_id.zipcode

    def generate_xlsx_report(self, workbook, data, docs):
        name_sheet = "EXCEL REPORT"
        data = self.get_report_data(data.get('date'))

        worksheet = workbook.add_worksheet(name_sheet)
        worksheet.set_column("A:ZZ", 25)
        self.draw_header(worksheet=worksheet, workbook=workbook)

        row = 1
        print(data)
        cell_format = workbook.add_format({'align': 'center', 'font_size': 10})
        currency_format = workbook.add_format({'num_format': '$#,##0.00', 'font_size': 10, 'align': 'center'})
        for item in data:
            col = 0
            worksheet.write(row, col, item.get('partner'), cell_format)
            worksheet.write(row, col + 1, item.get('product'), cell_format)
            worksheet.write(row, col + 2, item.get('price'), currency_format)
            worksheet.write(row, col + 3, item.get('standard_price'), currency_format)
            row += 1

    def get_standard_price(self, product_id):
        return self.env['product.product'].browse(product_id).standard_price
