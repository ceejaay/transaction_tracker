from test_model import TestModel

class TestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
        model = TestModel
