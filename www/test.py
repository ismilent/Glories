
class A(object):
    @classmethod
    def class_method(cls, **kwargs):
        print kwargs
        print cls(**kwargs)
    
    def update(self, commit=True):
        print 'update'
    
    def self_method(self):
        print self



a= A()
a.class_method(update=True)