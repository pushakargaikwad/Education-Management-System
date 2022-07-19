from odoo import models, fields, api, _

class Student(models.Model):
    _name = 'pg.student'
    _description = 'Student'
    _order = 'roll_number'


    name = fields.Char(string='Name', required=True)
    roll_number = fields.Char(string='Roll Number')
    language = fields.Many2one('res.lang', string='Mother Tongue')