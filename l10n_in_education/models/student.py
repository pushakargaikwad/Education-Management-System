from odoo import models, fields, api, _

class EMSStudent(models.Model):
    _inherit = 'ems.student'

    pan_card_no = fields.Char(string='PAN Card No.')
    aadhaar_card_no = fields.Char(string='Aadhaar Card No.')
    gr_number = fields.Char(string='GR Number')
    udise_no = fields.Char(string='U-DISE No.')
     

