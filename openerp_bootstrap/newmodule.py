from paste.script import templates
from paste.script.templates import var


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
        var('depends', 'Dependencies [space-separated module names]',default=''),
        var('is_web', 'Is web addon? [yes/no]', default='no'),    
    ]

    def pre(self, command, output_dir, vars):
        """
        Called before template is applied.
        """
        # import pdb;pdb.set_trace()
        depends = vars['depends'].split(' ')
        vars['is_web'] = vars['is_web'] == 'yes' and True or False
        if vars['is_web'] and not 'web' in depends:
            depends.append('web')
        vars['depends'] = [x for x in depends if x]