from odoo import models, fields, api, _

class AcademicYear(models.Model):
    _name = 'academic.year'
    _description = 'Academic Year'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    active = fields.Boolean(string='Active', default=True, help='If unchecked, it will allow you to hide the academic year record without removing it.')
