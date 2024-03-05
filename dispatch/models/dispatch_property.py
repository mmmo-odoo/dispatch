from odoo import fields, models

class DispatchProperty(models.Model):
    _name = "dispatch.property"
    _description = "Used for Vehicle Transportation"
    name = fields.Char(required = True)
    
