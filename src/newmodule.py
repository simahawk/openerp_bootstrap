from paste.script import templates
from templer.core.base import get_var
from templer.core.vars import var

class NewModule(templates.Template):

    egg_plugins = ['openerp_newmodule']
    summary = 'Template for creating a basic openerp package skeleton'
    required_templates = []
    _template_dir = 'templates/newmodule'
    use_cheetah = True

    vars = [
        var('module_name', 'Module name (like "Project Issue")',
            default='My Module'),
        var('description', 'One-line description of the module'),
        var('version', 'Version', default='1.0'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('category', 'Category'),
        var('website', 'Website'),
    ]
