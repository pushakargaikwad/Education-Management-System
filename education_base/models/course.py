from odoo import models, fields, api, _

class EMSCourse(models.Model):
    _name = 'ems.course'
    _description = 'Course'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True, help='If unchecked, it will allow you to hide the course record without removing it.')