# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def _get_purchase_price(self):
        """Overriden from `account_invoice_margin` method"""
        self.ensure_one()
        return (
            self.sale_line_ids.purchase_price
            or self.product_id.standard_price
        )

    @api.depends(
        "product_id", "product_uom_id", "sale_line_ids.purchase_price"
    )
    def _compute_purchase_price(self):
        """Exclude posted invoice lines depending on company setting values."""
        lines_posted = self.filtered(
            lambda ln: not ln.company_id.cost_sale_sync_invoice_posted
            and ln.parent_state == "posted"
        )
        return super(AccountMoveLine, self - lines_posted)._compute_purchase_price()
