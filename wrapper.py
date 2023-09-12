
class Wrapper:

    def __init__(self, activity_type=None, participants=None, minprice=None, maxprice=None, minaccessibility=None, maxaccessibility=None):
        self.type = activity_type
        self.participants = participants
        self.minprice = minprice
        self.maxprice = maxprice
        self.minaccessibility = minaccessibility
        self.maxaccessibility = maxaccessibility

        self.queries_dict = {"type": self.type,
                             "participants": self.participants,
                             "minprice": self.minprice,
                             "maxprice": self.maxprice,
                             "minaccessibility": self.minaccessibility,
                             "maxaccessibility": self.maxaccessibility}

    def get_activity(self):
        # Extract from "self.queries_dict" not None value. If all values equal None, get_activity method return random activity
        add = '&'.join(f"{querie}={self.queries_dict[querie]}" for querie in self.queries_dict if self.queries_dict[querie] != None )
        return f"http://www.boredapi.com/api/activity?{add}" if add else "http://www.boredapi.com/api/activity/"

