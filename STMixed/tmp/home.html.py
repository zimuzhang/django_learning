# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449218545.393
_enable_loop = True
_template_filename = 'E:\\mygit\\django_learning\\STMixed\\templates/home.html'
_template_uri = 'home.html'
_source_encoding = 'utf-8'
_exports = [u'site_css', u'site_script', u'site_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'site-template.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_css():
            return render_site_css(context._locals(__M_locals))
        def site_script():
            return render_site_script(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_css'):
            context['self'].site_css(**pageargs)
        

        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_script'):
            context['self'].site_script(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_css(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_css():
            return render_site_css(context)
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_script(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_script():
            return render_site_script(context)
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"37": 1, "42": 3, "75": 8, "47": 6, "81": 5, "87": 5, "57": 2, "26": 0, "93": 87, "69": 8, "63": 2}, "uri": "home.html", "filename": "E:\\mygit\\django_learning\\STMixed\\templates/home.html"}
__M_END_METADATA
"""
