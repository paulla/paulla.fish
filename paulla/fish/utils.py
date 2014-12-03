# -*- coding: utf-8 -*-
import argparse
import ConfigParser
import sqlite3
import datetime
import os.path

import couchdbkit
import magic

from paulla.fish.models import ToStore

def migration():
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf',
                        help='wsgi conf file')

    parser.add_argument('--database',
                        help='sqlite database')

    parser.add_argument('--upload-dir',
                        help='directory where file are stored')

    args = parser.parse_args()

    config = ConfigParser.RawConfigParser()
    config.read(args.conf)

    server = couchdbkit.Server(config.get('app:main', 'couchdb.url'))
    db = server.get_or_create_db(config.get('app:main','couchdb.db'))

    ToStore.set_db(db)

    sqlDB = sqlite3.connect(args.database)

    cursor = sqlDB.execute("select id, fdescr, fpath, fid, fname from tasks where closed = 0")

    for row in cursor.fetchall():
        id_, fdescr, fpath, fid, fname = row
        todo = ToStore(_id=id_,
                      description=fdescr,
                      filename=fname,
                      dtInserted=datetime.datetime.now()
                      )

        todo.save()

        with open(os.path.join(args.upload_dir, fid), 'rb') as attachment:
            with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as guess:
                mime = guess.id_buffer(attachment.read(1024))
            attachment.seek(0)
            todo.put_attachment(attachment, 'attachment', content_type=mime)
