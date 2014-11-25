import os
import logging
import datetime


from pyramid.httpexceptions import HTTPFound
from pyramid.threadlocal import get_current_registry
from pyramid.view import view_config

from pyramid.renderers import get_renderer

import magic

import couchdbkit
from couchdbkit.designer import push

from models import ToStore

settings = get_current_registry().settings
print settings

# server object
server = couchdbkit.Server(settings['couchdb.url'])

# create database
db = server.get_or_create_db(settings['couchdb.db'])
ToStore.set_db(db)

here = os.path.dirname(__file__)
for view in ['list']:
    path = os.path.join(here, 'couchdb', '_design', view)
    push(path, db)

@view_config(route_name='listing', renderer='templates/listing.pt')
def list_view(request):
    return {"layout": site_layout(),
            'file_list': []}


@view_config(route_name='new', renderer='json', request_method='POST')
def new_view(request):
    if request.POST.get('fdescr', 'fname'): # TODO
        descripton = request.POST['description']
        filename = request.POST['filename'].filename

        inputFile = request.POST['filename'].file

        toStore = ToStore(descripton=descripton,
                          filename=filename,
                          dtInserted=datetime.datetime.now())
        toStore.save()
        mime = ''
        with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as guess:
            mime = guess.id_buffer(inputFile.read(1024))

        inputFile.seek(0)

        toStore.put_attachment(inputFile, 'attachment', content_type=mime)

        return HTTPFound(location=request.route_path('listing'))
    else:
        request.session.flash(
            'Please enter a short description for the file!'
            )
    return {}


@view_config(route_name='close')
def close_view(request):
    task_id = int(request.matchdict['id'])
    request.db.execute("update tasks set closed = ? where id = ?",
                       (1, task_id))
    request.db.commit()
    request.session.flash('File was successfully marked for delete!')
    return HTTPFound(location=request.route_path('listing'))


@view_config(route_name='dl')
def dl_page(request):
    task_id = int(request.matchdict['id'])
    rs = request.db.execute(
        "select fdescr, fpath, fid, fname from tasks where id = %i"
        % (task_id)
        )
    file_data = fdescr, fpath, fid, fname = rs.fetchone()
    response = FileResponse(
        os.path.join(fpath, fid),
        request=request,
        )
    return response


@view_config(route_name='detail', renderer='templates/detail.pt')
def detail_page(request):
    task_id = int(request.matchdict['id'])
    rs = request.db.execute(
        "select id, fdescr, fpath, fid, fname from tasks where id = %i"
        % (task_id)
        )
    file_data = id, fdescr, fpath, fid, fname = rs.fetchone()
    return {'layout': site_layout(),
            'file_data': file_data}


@view_config(context='pyramid.exceptions.NotFound', renderer='templates/notfound.pt')
def notfound_view(request):
    request.response.status = '404 Not Found'
    return {'layout': site_layout()}


# s# ubscribers
# @subscriber(NewRequest)
# def new_request_subscriber(event):
#     request = event.request
#     settings = request.registry.settings
#     request.db = sqlite3.connect(settings['db'])
#     request.add_finished_callback(close_db_connection)


# def close_db_connection(request):
#     request.db.close()


# @subscriber(ApplicationCreated)
# def application_created_subscriber(event):
#     log.warn('Initializing database...')
#     with open(os.path.join(here, 'schema.sql')) as f:
#         stmt = f.read()
#         settings = event.app.registry.settings
#         db = sqlite3.connect(settings['db'])
#         db.executescript(stmt)
#         db.commit()

"""
@subscriber(BeforeRender)
def add_base_template(event):
    base = get_renderer('templates/base.pt').implementation()
    listing = get_renderer('templates/listing.pt').implementation()
    event.update({'base': base,
                    'listing':'listing',
    })
"""

def site_layout():
    renderer = get_renderer("templates/layout.pt")
    layout = renderer.implementation().macros['layout']
    return layout

def hide_element(request):
    return (
        "javascript:document.getElementById('%s').style.display = 'none'"
        % element
    )

def show_element(request):
    return (
        "javascript:document.getElementById('%s').style.display = 'block'"
        % element
    )
