from openerp import models, fields, api

'''
This module create model of Course
'''


class Course(models.Model):
    '''
    This class create model of Course
    '''
    _name = 'openacademy.course'  # Model odoo name

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
