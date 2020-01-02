from odoo import api, fields, models


class Employee(models.Model):
    _name = 'employee'
    _description = 'Employees'
    _rec_name = 'emp_name'

    emp_name = fields.Char(required=True)
    its_employees = fields.One2many('employee', 'its_employer', string='Lower Segment')
    its_employer = fields.Many2one('employee', string='Upper Segment')
    employer_level = fields.Integer(related='its_employer.level', default=0)
    level = fields.Integer(compute='_comp_level', default=0)

    active = fields.Boolean(default=True)

    @api.depends('its_employer')
    def _comp_level(self):
        for record in self:
            if not record.its_employer:
                record.level = 1
            else:
                record.level = record.employer_level + 1
