from odoo import models, fields, api, Command


class ComputedChild(models.TransientModel):
    _name = "computed_child"
    msg = fields.Char()


class DemoParent(models.TransientModel):
    _name = "demo_parent"

    number = fields.Integer(help="Tells, how many children/messages to generate")
    child_ids = fields.One2many(
        compute="_compute_child_ids", comodel_name="computed_child"
    )

    @api.depends("number")
    def _compute_child_ids(self):
        for rec in self:
            children_data = [{"msg": f"Child {i}"} for i in range(rec.number)]
            children = self.env["computed_child"].create(children_data)
            rec.child_ids = children

    # def onchange(self, values, field_names, fields_spec):
    #     # dumb workaround to remove dangling previous records in UI (not in DB)
    #     # Let's guess that no more than 777 children were created after initial ones
    #
    #     # Command.clear() and Command.set(..)  seems not works in o2m UI :shrug:
    #     # so we just insert Command.DELETE for arbitrary amount of previous ids
    #
    #     result = super().onchange(values, field_names, fields_spec)
    #
    #     children = result.get("value", {}).get("child_ids")
    #     new_info_ids = [
    #         id
    #         for (cmd, id, data) in children
    #         if cmd in [Command.LINK, Command.CREATE]
    #     ]
    #
    #     min_new_id = min(new_info_ids)
    #     potentially_shown_previous_ids = range(min_new_id - 777, min_new_id)
    #     children[:0] = [Command.delete(id) for id in potentially_shown_previous_ids]
    #
    #     return result
