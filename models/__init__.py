from odoo import models, fields, api, Command


class ComputedChild(models.TransientModel):
    _name = 'computed_child'
    msg = fields.Char()


class DemoParent(models.TransientModel):
    _name = 'demo_parent'

    number = fields.Integer(help="Tells, how many children/messages to generate")
    child_ids = fields.One2many(
        compute="_compute_child_ids", comodel_name="computed_child"
    )

    @api.depends("number")
    def _compute_child_ids(self):
        for rec in self:
            children_data = [{"msg": f"Child {i}"} for i in range(rec.number)]
            children = self.env['computed_child'].create(children_data)
            rec.child_ids = children
