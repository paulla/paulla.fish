import couchdbkit


class ToStore(couchdbkit.Document):
    description = couchdbkit.StringProperty()
    dtInserted = couchdbkit.DateTimeProperty()
    filename = couchdbkit.StringProperty()
