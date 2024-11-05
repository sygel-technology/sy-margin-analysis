import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-margin-analysis",
    description="Meta package for sygel-technology-sy-margin-analysis Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_invoice_margin_sale_sync>=15.0dev,<15.1dev',
        'odoo-addon-sync_sale_picking_cost>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
