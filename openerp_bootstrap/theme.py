import os
import shutil

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
        # TODO: look at templer.core to see how to handle bool vars
        # and evaluate if we should depend on it
        for k in ['has_js','has_css','has_xml']:
            vars[k] = vars[k] == 'yes' and True or False
        depends = vars['depends'].split(' ')
        if not 'web' in depends:
            depends.append('web')
        vars['depends'] = [x for x in depends if x]
        vars['normalized_name'] = vars['package']

    def post(self, command, output_dir, vars):
        for i in ('css','js','xml'):
            if not vars['has_'+i]:
                # remove it from static             
                path = os.path.join(output_dir, 'static')
                try:
                    rmpath = os.path.join(path, i)
                    shutil.rmtree(rmpath)
                    print '%s not required, removed dir %s' % (i,rmpath)
                except OSError, e:
                    msg = """WARNING: Error in template rendering:"""
                    print msg + str(e)