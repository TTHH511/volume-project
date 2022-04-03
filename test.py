from flight_query import FlightQueryService
import unittest

class testQuery( unittest.TestCase ):

    def testQuery( self ):
        fqs = FlightQueryService()

        # a common case
        self.assertEqual(
            fqs.findFlightPath([['IND', 'EWR'], ['SFO', 'ATL'], ['GSO', 'IND'], ['ATL', 'GSO']]),
            ['SFO', 'EWR'],
                        )


        # case with a cycle 
        self.assertEqual(
            fqs.findFlightPath(
                [
                    ['A', 'B'],
                    ['B', 'C'],
                    ['C', 'D'],
                    ['D', 'A'],
                    ['E', 'A'],
                    ['A', 'F'],
                ]
            ),
            ['E', 'F'],
        )

    def testRaise( self ):
        fqs = FlightQueryService()

        with self.assertRaises(Exception):
            fqs.findFlightPath([['IND', 'EWR'], ['EWR', 'IND']])

        with self.assertRaises(Exception):
            fqs.findFlightPath([['EWR', 'IND'], ['EWR', 'IND']])

    
if __name__ == '__main__':
    unittest.main()