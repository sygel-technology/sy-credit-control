import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-credit-control",
    description="Meta package for sygel-technology-sy-credit-control Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_invoice_overdue_warn_public>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_overdue_warn_sale_public>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
