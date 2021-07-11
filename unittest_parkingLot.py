import unittest
from main import ParkingLot, Car, Bike


class TestParkingLot(unittest.TestCase):

    def testPark(self):
        parkingLotObj = ParkingLot(8, 40)
        res2 = parkingLotObj.ParkVehicle(Car("HR26DQ8891", "Hyundai"))
        res3 = parkingLotObj.ParkVehicle(Bike("HR29AL7654", "Hero"))

        self.assertEqual(res2, True)
        self.assertEqual(res3, True)


    def testLeaveOperation(self):
        parkingLotObj = ParkingLot(8, 40)
        self.assertTrue(parkingLotObj.ParkVehicle(Car("HR26DQ8891", "Hyundai")))
        self.assertTrue(parkingLotObj.LeaveOperation(Car("HR26DQ8891", "Hyundai")))
        self.assertEqual(parkingLotObj.LeaveOperation(Car("HR26DQ8891", "Hyundai")), None)


    def testCompanyParked(self):
        parkingLotObj = ParkingLot(8, 40)
        self.assertTrue(parkingLotObj.ParkVehicle(Car("HR26DQ8891", "Hyundai")))
        self.assertEqual(parkingLotObj.CompanyParked("Hyundai"), [Car("HR26DQ8891", "Hyundai")])
        print(parkingLotObj.CompanyParked("Hyundai"))

        
    def test(self):
        parkingLotObj = ParkingLot(2, 20)
        self.assertTrue(parkingLotObj.ParkVehicle(Car("HR290007", "Hyundai")))
        self.assertEqual(parkingLotObj.CompanyParked("Hyundai"), [Car("HR290007", "Hyundai")])
        self.assertTrue(parkingLotObj.LeaveOperation(Car("HR290007", "Hyundai")))
        self.assertEqual(parkingLotObj.CompanyParked("Hyundai"), [])


if __name__ == '__main__':
    unittest.main()