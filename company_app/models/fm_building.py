from odoo import api, fields, models
import math


class Building(models.Model):
    _name = 'fm.building'
    _description = 'Buildings'

    building_name = fields.Char(required=True)
    building_no = fields.Char(required=True)
    building_dimension = fields.Char(string='Dimension')
    construction_year = fields.Integer(string='Construction Year')
    structural_system = fields.Char(string='Hey')
    office_area_as_mt_square = fields.Float()
    under_root_area_as_meter = fields.Float(string='Meter: ', compute='_mt_sqr_to_mt')
    under_root_area_as_feet = fields.Float(string='Feet: ', compute='_mt_to_feet')

    active = fields.Boolean()
    building_ids = fields.One2many('employee.building.assignment', 'building_id', string='Building')

    @api.depends('office_area_as_mt_square')
    def _mt_sqr_to_mt(self):
        self.under_root_area_as_meter = math.sqrt(self.office_area_as_mt_square)

    @api.depends('under_root_area_as_meter')
    def _mt_to_feet(self):
        self.under_root_area_as_feet = self.under_root_area_as_meter / .3048 % 1 * 12
