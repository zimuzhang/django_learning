# -*- coding:utf8 -*-

from django.conf import settings
from django.template.loader import BaseLoader
from django.template  import TemplateDoesNotExist
from django.utils.importlib import import_module
from mako.lookup import TemplateLookup
from mako.exceptions import TopLevelLookupException

app_template_dirs = []

#遍历INSTALL_APP
for app in settings.INSTALLED_APPS:
    if app.startwiths('django'):
        continue
    try:
        mod = import_module(app)
    except ImportError, e:
        raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))
    template_dir = os.path.join(os.path.dirname(mod.__file__), 'templates')
    if os.path.isdir(template_dir):
        app_template_dirs.append(template_dir)

app_template_dirs = tuple(app_template_dirs)

class Template(object):
    def __init__(self, template):
        self.template = template

    def render(self, context):
        data = {}
        for d in context:
            data.update(d)
        if 'self' in data:
            data.pop('self')
        return self.template.render(**data)

class MakoTemplateLoader(BaseLoader):
    is_usable = True

    template_dirs = getattr(settings,'MAKO_TEMPLATE_DIRS', settings.TEMPLATE_DIRS)
    input_encoding = getattr(settings, "MAKO_INPUT_ENCODING", settings.DEFAULT_CHARSET)
    output_encoding = getattr(settings, "MAKO_OUTPUT_ENCODING", settings.DEFAULT_CHARSET)
    filesystem_checks = getattr(settings,'MAKO_FILESYSTEM_CHECKS', settings.DEBUG)
    module_dir = getattr(settings, "MAKO_MODULE_DIR", None)
    
    # 追加app目录下面的templates目录
    parameters = {
        'directories'         : template_dirs + app_template_dirs,
        'input_encoding'      : input_encoding,
        'output_encoding'     : output_encoding, 
        'filesystem_checks'   : filesystem_checks,
        'module_directory'    : module_dir,
    }
    lookup = TemplateLookup(**parameters)
    
    def load_template(self, template_name, template_dirs=None):
        try:
            template = self.lookup.get_template(template_name)
            return Template(template), template.filename
        except TopLevelLookupException:
            raise TemplateDoesNotExist