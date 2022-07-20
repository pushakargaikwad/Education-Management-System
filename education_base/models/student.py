from odoo import models, fields, api, _

class EMSStudent(models.Model):
    _name = 'ems.student'
    _description = 'Student'
    _order = 'roll_number'


    name = fields.Char(string='Name', required=True)
    roll_number = fields.Char(string='Roll Number')
    language = fields.Many2one('res.lang', string='Mother Tongue')
    active = fields.Boolean(string='Active', default=True, help='If unchecked, it will allow you to hide the student record without removing it.')