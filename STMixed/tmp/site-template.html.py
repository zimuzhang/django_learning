# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1449303383.165
_enable_loop = True
_template_filename = u'E:\\mygit\\django_learning\\STMixed\\templates/site-template.html'
_template_uri = u'site-template.html'
_source_encoding = 'utf-8'
_exports = [u'site_css', u'site_name', u'site_script', u'site_content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_css():
            return render_site_css(context._locals(__M_locals))
        def site_name():
            return render_site_name(context._locals(__M_locals))
        def site_script():
            return render_site_script(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="zh-cn">\r\n<head>\r\n    <meta chart-set="utf-8"></meta>\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge"></meta>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1">\r\n    <title>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_name'):
            context['self'].site_name(**pageargs)
        

        __M_writer(u'\r\n    </title>\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'bootstrap/css/bootstrap.min.css">\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'work/css/work.css">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_css'):
            context['self'].site_css(**pageargs)
        

        __M_writer(u'\r\n</head>\r\n<body>\r\n    <!-- head -->\r\n    <div class="navbar navbar-default">\r\n      <div class="container">\r\n        <div class="row">\r\n            <div class="col-lg-6">\r\n                <div class="col-lg-6">\r\n                title\r\n                </div>\r\n            </div>\r\n            <div class="col-lg-6">\r\n                <nav>\r\n                    <ul class="nav navbar-nav">\r\n                        <li><a>test1</a></li>\r\n                        <li><a>test2</a></li>\r\n                        <li><a>test3</a></li>\r\n                    </ul>\r\n                </nav>\r\n            </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n    <!-- content -->\r\n    <div class="content-preview">\r\n        <div class="container">\r\n            <div class="row">\r\n                <div class="col-lg-4 col-sm-6">\r\n                    <div class="preview">\r\n                        <div class="img">\r\n                        </div>\r\n                        <div class="dec">\r\n                            <h3>Angular Demo</h3>\r\n                            <p>the note of angular</p>\r\n                            <div class="col-lg-4"></div>\r\n                            <div class="col-lg-4">\r\n                                <a class="btn btn-info" href="#">\u8fdb\u5165</a>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n                <div class="col-lg-4 col-sm-6">\r\n                    <div class="preview">\r\n                        <div class="img">\r\n                        </div>\r\n                        <div class="dec">\r\n                            <h3>JavaScript Demo</h3>\r\n                            <p>the note of JavaScript</p>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n                <div class="col-lg-4 col-sm-6">\r\n                    <div class="preview">\r\n                        <div class="img">\r\n                        </div>\r\n                        <div class="dec">\r\n                            <h3>Data Demo</h3>\r\n                            <p>the note of python data</p>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer(u'\r\n\r\n    <!-- foot -->\r\n\r\n    <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>\r\n    <script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_script'):
            context['self'].site_script(**pageargs)
        

        __M_writer(u'\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_css(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_css():
            return render_site_css(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_name(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_name():
            return render_site_name(context)
        __M_writer = context.writer()
        __M_writer(u'Learning')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_script(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_script():
            return render_site_script(context)
        __M_writer = context.writer()
        __M_writer(u'\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 8, "35": 10, "36": 10, "37": 11, "38": 11, "105": 94, "43": 12, "76": 8, "15": 0, "48": 77, "82": 83, "53": 84, "88": 83, "59": 12, "70": 8, "29": 1, "94": 77}, "uri": "site-template.html", "filename": "E:\\mygit\\django_learning\\STMixed\\templates/site-template.html"}
__M_END_METADATA
"""
