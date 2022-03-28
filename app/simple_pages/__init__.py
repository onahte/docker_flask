from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_pages', __name__,
                        template_folder='templates',static_folder='static')


@simple_pages.route('/', defaults={'page': 'index'})
@simple_pages.route('/<page>')
def show(page):
    lpage = ''
    lgit = ''
    ldock = ''
    lpy = ''
    lci = ''
    loop = ''
    laaa = ''
    lsolid = ''
    lplint = ''

    if page == 'index':
        lpage = 'active'
    elif page == 'git':
        lgit = 'active'
    elif page == 'docker':
        ldock = 'active'
    elif page == 'python':
        lpy = 'active'
    elif page == 'cicd':
        lci = 'active'
    elif page == 'oop':
        loop = 'active'
    elif page == 'aaa':
        laaa = 'active'
    elif page == 'solid':
        lsolid = 'active'
    elif page == 'plint':
        lplint = 'active'

    try:
        return render_template('%s.html' % page, lpage=lpage, lgit=lgit, ldock=ldock, lpy=lpy, lci=lci, loop=loop,
                               laaa=laaa, lsolid=lsolid, lplint=lplint)
    except TemplateNotFound:
        abort(404)
