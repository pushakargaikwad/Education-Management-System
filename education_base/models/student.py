from odoo import models, fields, api, _

class EMSStudent(models.Model):
    _name = 'ems.student'
    _description = 'Student'
    _order = 'roll_number'


    name = fields.Char(string='Name', required=True)
    roll_number = fields.Char(string='Roll Number')
    language = fields.Many2one('res.lang', string='Mother Tongue')
    active = fields.Boolean(string='Active', default=True, help='If unchecked, it will allow you to hide the student record without removing it.')
    gender = fields.Many2one('res.gender',string='Gender')
    birth_date = fields.Date(string='Birthdate')
    place_of_birth = fields.Char(string='Place of Birth')
    blood_group = fields.Selection([('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')], string='Blood Group')
    is_alumni = fields.Boolean('Alumni Student?')

    # Documents
    passport_no = fields.Char(string='Passport No.')
    driving_license_no = fields.Char(string='Driving License No.')


    # Academic Information
    course_id = fields.Many2one('ems.course', string='Course')
    standard_id = fields.Many2one('ems.standard', string='Standard')

