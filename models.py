from pony.orm import *


db = Database()


class Post(db.Entity):
    article_id = Required(unicode)
    article_title = Required(unicode)
    date = Required(unicode)
    author = Required(unicode)
    content = Required(unicode)


db.bind('sqlite', 'database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

