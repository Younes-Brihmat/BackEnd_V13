

{
    "name": "Backend Theme V14",
    "summary": "Openworx Material Backend Theme V14",
    "version": "14.0.0.1",
    "category": "Theme/Backend",
    "website": "http://www.hsn-tech.com",
	"description": """
		Openworx Material Backend theme for Odoo 14.0 community edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "HSN-Tech",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'web_responsive',

    ],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
		'views/users.xml',
        'views/sidebar.xml',
    ],

}

