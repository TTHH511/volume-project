class FlightQueryService():

    def findFlightPath(self, query):
        ref = {}
        for start, end in query:
            ref[start] = ref.get(start, 0) + 1
            ref[end] = ref.get(end, 0) - 1
            if ref[start] == 0:
                ref.pop(start)
            if ref[end] == 0:
                ref.pop(end)
            #print(ref)

        start = []
        end = []
        for k, v in ref.items():
            if v == 1:
                start.append(k)
            elif v == -1:
                end.append(k)
            else:
                raise Exception( "multiple flights found for departure/desination {}".format(k) )

        if not(len(start) == 1 and len(end) == 1):
            raise Exception("not exactly 1 departure & destination found" )

        return [start[0], end[0]]