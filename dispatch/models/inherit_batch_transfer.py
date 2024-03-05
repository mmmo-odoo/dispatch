from odoo import api, fields, models

class BatchTransfer(models.Model):
    _inherit = "stock.picking.batch"
    dock = fields.Many2one("dispatch.property.doc")
    vehicle_id = fields.Many2one("fleet.vehicle")
    vehicle_category = fields.Many2one("fleet.vehicle.model.category")
    weight = fields.Integer(compute = "_compute_weight")
    # volume = fields.Float(compute = "_compute_volume")

    @api.depends("vehicle_category", "picking_ids")
    def _compute_weight(self):
        for line in self:
            total_weight = 0
            if line.picking_ids:
                total_weight = sum(line.picking_ids.mapped("weight"))
            if total_weight > 0 and line.vehicle_category.max_weight > 0:
                line.weight = (total_weight * 100) / line.vehicle_category.max_weight
            else:
                line.weight = 0