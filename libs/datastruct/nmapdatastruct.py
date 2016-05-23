
class NmapHostStruct(object):
    taskid = None
    inserted = None
    domain = None
    address = None
    is_up = None
    os = None

    def __str__(self):
        return str(self.__dict__)

class NmapServiceStruct(object):
    taskid = None
    inserted = None
    address = None
    port = None
    service = None
    state = None
    protocol = None
    product = None
    product_version = None
    product_extrainfo = None
    scripts_results = None

    def __str__(self):
        return str(self.__dict__)