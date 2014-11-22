import couchdbkit


class ToStore(couchdbkit.Document):
    description = couchdbkit.StringProperty()
    path = couchdbkit.StringProperty()
    dtInserted = couchdbkit.DateTimeProperty()
    closed = couchdbkit.BooleanProperty()
    name = couchdbkit.StringProperty()
