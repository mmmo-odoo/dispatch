from odoo import fields, models

class DispatchProperty(models.Model):
    _name = "dispatch.property"
    _description = "Control Dispatch Management System"
    name = fields.Char(required = True)
    max_weight = fields.Integer(string="Max Weight (Kg)")
    max_volume = fields.Integer(string="Max Volume (m^3)")
