import json

class Adapter:
    """
        The Adapter is responsible for serialization and deserialization of the Transport Network Model (TNM) defined in RFC0020.
        It follows the following interface:
            from_json(JSON model)
            to_json(data)
        All Microservices following TNM must have an Adapter implementing this interface.
    """

    def __init__(self):
        """
            The Adapter constructor. Currently not in use.
        """
        pass

    def from_json(self, options):
        """
            Converts the TNM to some internal representation.
            In this Creator service, it converts some options (defined in RFC0020) from JSON to a python dictionary.
        """
        if options == None:
            options = {}
        return json.loads(options)

    def to_json(self, **data_tables):
        """ 
            Converts the internal representation from the service to the TNM.
            In this Creator service, it converts data from the Database to the initial JSON schema following the TNM.
        """
        pass