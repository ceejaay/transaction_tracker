

class TestModel(db.Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
