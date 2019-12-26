from odoo import api, fields, models


class EmployeeBuildingAssignment(models.Model):
    _name = 'employee.building.assignment'
    _rec_name = 'display_names'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    emp_name = fields.Char(related='employee_id.name')

    building_id = fields.Many2one('fm.building', string='Building', required=True)
    building_name = fields.Char(related='building_id.building_name')

    assignment_start_date = fields.Date()

    assignment_end_date = fields.Date()

    display_names = fields.Char(compute='_display_name')

    # @api.depends('emp_name', 'building_name')
    @api.depends('assignment_start_date')
    @api.one
    def _display_name(self):
        self.display_names = self.building_name + " " + self.emp_name
