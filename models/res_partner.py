from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    library_loan_count = fields.Integer(compute='_compute_library_loan_count', string='Libro(s)')

    def _compute_library_loan_count(self):
        loan_model = self.env['library.loan']
        for partner in self:
            partner.library_loan_count = loan_model.search_count([('res_partner_id', '=', partner.id)])

    def action_view_library_loan(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Library Loans'),
            'res_model': 'library.loan',
            'view_mode': 'tree,form',
            'domain': [('res_partner_id', '=', self.id)],
            'context': {'default_res_partner_id': self.id},
        }
