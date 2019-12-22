from odoo import api, fields, models


class EmployeeBuildingAssignment(models.Model):
    _name = 'employee.building.assignment'

    employee_id = fields.Many2one('hr.employee', string='employee')

    building_id = fields.Many2one('fm.building', string='Hey')

    assignment_start_date = fields.Date()

    assignment_end_date = fields.Date()
