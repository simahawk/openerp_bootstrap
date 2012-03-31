from paste.script import templates
from paste.script.templates import var


class Theme(templates.Template):

    egg_plugins = ['openerp_theme']
    summary = 'Template for creating a basic openerp theme skeleton'
    required_templates = []
    _template_dir = 'templates/theme'
    use_cheetah = True

    vars = [
        var('module_name', 'Module name (like "My Theme")',
            default='My Theme'),
        var('description', 'One-line description of the module'),
        var('version', 'Version', default='1.0'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('category', 'Category'),
        var('website', 'Website'),
        var('depends', 'Dependencies [space-separated module names]',default=''),
        var('has_css', 'Needs CSS? [yes/no]', default='yes'),    
        var('has_js', 'Needs Javascript? [yes/no]', default='yes'),
        var('has_xml', 'Needs QWeb XML? [yes/no]', default='no'),
    ]

    def pre(self, command, output_dir, vars):
        """
        Called before template is applied.
        """
        # import pdb;pdb.set_trace()
        depends = vars['depends'].split(' ')
        if not 'web' in depends:
            depends.append('web')
        vars['depends'] = [x for x in depends if x]
        vars['normalized_name'] = vars['package']