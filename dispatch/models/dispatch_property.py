from odoo import fields, models

class DispatchProperty(models.Model):
    _name = "dispatch.property"
    _description = "Control Dispatch Management System"
    name = fields.Char(required = True)