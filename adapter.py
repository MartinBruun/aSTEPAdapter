class Adapter:
    """
        The Adapter is responsible for serialization and deserialization of the Transport Network Model (TNM) defined in RFC0020.
        It follows the following interface:
            to_json(data)
            from_json(JSON model)
        All Microservices following TNM must have an Adapter implementing this interface.
    """

    def to_json(**data):
        """ 
            Converts the internal representation from the service to the TNM.
            In this Creator service, it converts data from the Database to the initial JSON schema following the TNM.
        """
        pass

    def from_json(options):
        """
            Converts the TNM to some internal representation.
            In this Creator service, it converts some options (defined in RFC0020) from JSON to a python dictionary.
        """
        return options.json()