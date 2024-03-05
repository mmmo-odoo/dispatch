from odoo import api, fields, models

class BatchTransfer(models.Model):
    _inherit = "stock.picking.batch"
    dock = fields.Many2one("dispatch.property.doc")
    vehicle_id = fields.Many2one("fleet.vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category")
    weight = fields.Integer(compute = "_compute_weight", store="True")
    volume = fields.Float(compute = "_compute_volume", store = "True")
    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')

    @api.depends("vehicle_category_id", "move_line_ids")
    def _compute_weight(self):
        for line in self:
            if line.vehicle_category_id :
                product_weight = 0
                for product in line.move_line_ids:
                    product_weight += product.product_id.weight * product.quantity
                line.weight = (product_weight / line.vehicle_category_id.max_weight) * 100
            else :
                line.weight = 0.0

    @api.depends("vehicle_category_id", "move_line_ids")
    def _compute_volume(self):
        for line in self:
            if(line.vehicle_category_id):
                product_volume = 0
                for products in line.move_line_ids:
                    product_volume += products.product_id.volume * products.quantity
                line.volume = (product_volume / line.vehicle_category_id.max_volume) * 100
            else :
                line.volume = 0.0
    
    @api.depends("name", "weight", "volume")
    def _compute_display_name(self):
        for line in self:
            name = f"{line.name}({line.weight}kg, {line.volume}m\u00B3)"
            line.display_name = name

                