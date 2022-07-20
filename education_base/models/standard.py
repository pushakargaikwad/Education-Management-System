from odoo import models, fields, api, _

class EMSStandard(models.Model):
    
    '''
    Depending on region this can have different names
    . Class
    . Standard
    . Year
    '''

    _name = 'ems.standard'
    _description = 'Standard'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    course = fields.Many2one('ems.course', string='Course')