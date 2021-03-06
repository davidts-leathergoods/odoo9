# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv
from openerp.tools.translate import _

class purchase_config_settings(osv.osv_memory):
    _name = 'purchase.config.settings'
    _inherit = 'res.config.settings'

    _columns = {
        'group_product_variant': fields.selection([
            (0, "No variants on products"),
            (1, 'Products can have several attributes, defining variants (Example: size, color,...)')
            ], "Product Variants",
            help='Work with product variant allows you to define some variant of the same products, an ease the product management in the ecommerce for example',
            implied_group='product.group_product_variant'),
        'group_uom':fields.selection([
            (0, 'Products have only one unit of measure (easier)'),
            (1, 'Some products may be sold/puchased in different units of measure (advanced)')
            ], "Units of Measure",
            implied_group='product.group_uom',
            help="""Allows you to select and maintain different units of measure for products."""),
        'group_costing_method':fields.selection([
            (0, 'Set a fixed cost price on each product'),
            (1, "Use a 'Fixed', 'Real' or 'Average' price costing method")
            ], "Costing Methods",
            implied_group='stock_account.group_inventory_valuation',
            help="""Allows you to compute product cost price based on average cost."""),
        'module_purchase_requisition': fields.selection([
            (0, 'Purchase propositions trigger draft purchase orders to a single supplier'),
            (1, 'Allow using call for tenders to get quotes from multiple suppliers (advanced)')
            ], "Calls for Tenders",
            help="Calls for tenders are used when you want to generate requests for quotations to several vendors for a given set of products.\n"
                 "You can configure per product if you directly do a Request for Quotation "
                 "to one vendor or if you want a Call for Tenders to compare offers from several vendors."),
        'group_warning_purchase': fields.selection([
            (0, 'All the products and the customers can be used in purchase orders'),
            (1, 'An informative or blocking warning can be set on a product or a customer')
            ], "Warning", implied_group='purchase.group_warning_purchase'),
        'module_stock_dropshipping': fields.selection([
            (0, 'Suppliers always deliver to your warehouse(s)'),
            (1, "Allow suppliers to deliver directly to your customers")
            ], "Dropshipping",
            help='\nCreates the dropship Route and add more complex tests\n'
                 '-This installs the module stock_dropshipping.'),
        'group_manage_vendor_price': fields.selection([
            (0, 'Manage vendor price on the product form'),
            (1, 'Allow using and importing vendor pricelists')
            ], "Vendor Price", 
            implied_group="purchase.group_manage_vendor_price"),
    }
