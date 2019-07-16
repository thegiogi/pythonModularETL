from Source import Source

CONN_STR = "connection_string"
KWARGS_DESC = "must specify connection string as {cstr}".format(cstr=CONN_STR)


class SQLSource(Source):
    def read(self):
        pass

    def __init__(self, **kwargs: KWARGS_DESC):
        super().__init__(**kwargs)
        self.conn_str = self.properties[CONN_STR]



s = SQLSource(connection_string="oriva")
print(s.conn_str)
