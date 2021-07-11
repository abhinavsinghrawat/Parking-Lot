from enum import Enum

class VehicleType(Enum):
	CAR = 1
	BIKE = 2

# Vehicle class with attributes as license plate, company name and type of vehicle 
class Vehicle:
	def __init__(self, licensePlate, companyName, typeofVehicle):
		self.licensePlate = licensePlate
		self.companyName = companyName
		self.typeofVehicle = typeofVehicle

	''' Overwriting __eq__ dunder method to check if two vehicles objects are same on the basis of 
	license plate, company name and type of vehicle'''
	def __eq__(self, other):
		if other is None:
			return False
		if self.licensePlate != other.licensePlate:
			return False
		if self.companyName != other.companyName:
			return False
		if self.typeofVehicle != other.typeofVehicle:
			return False
		return True

class Car(Vehicle):
	def __init__(self, licensePlate, companyName):
		Vehicle.__init__(self, licensePlate, companyName, VehicleType.CAR)

class Bike(Vehicle):
	def __init__(self, licensePlate, companyName):
		Vehicle.__init__(self, licensePlate, companyName, VehicleType.BIKE)

class Slot:
	def __init__(self, lane, slotNumber, typeofVehicle):
		self.lane = lane
		self.slotNumber = slotNumber
		self.vehicle = None
		self.typeofVehicle = typeofVehicle

	def isAvailable(self):
		return self.vehicle == None

	def park(self, vehicle):
		if self.typeofVehicle == vehicle.typeofVehicle:
			self.vehicle = vehicle
			return True
		else:
			return False

	def removeVehicle(self):
		self.vehicle = None
		return self.vehicle

	def getVehicle(self):
		return self.vehicle

# Level class with attributes as floor number, lane and slot
# Note : 10 slots make 1 lane
class Level:
	def __init__(self, floorNumber, noOfSlots):
		self.floorNumber = floorNumber
		self.slotsPerLane = 10
		self.lanes = noOfSlots / self.slotsPerLane
		self.parkingSlots = set()
		self.availableSlots = []

		# To check available slots in a lane
		for lane in range(int(self.lanes)):
			for i in range (self.slotsPerLane):
				import random
				self.availableSlots.append(Slot(lane, i, random.choice(list(VehicleType))))

	# To park vehicle if slot is available
	def park(self, vehicle):
		for slot in self.availableSlots:
			if slot.park(vehicle):
				return True
		return False

	# To remove vehicle from slot
	def remove(self, vehicle):
		for slot in self.availableSlots:
			if slot.getVehicle() == vehicle:
				slot.removeVehicle()
				return True
		return False

	# To get company name for the vehicle parked at available slot
	def company(self, companyName):
		vehicles = []
		for slot in self.availableSlots:
			vehicle = slot.getVehicle()
			if vehicle is not None and vehicle.companyName == companyName:
				vehicles.append(vehicle)
		return vehicles

# Parking lot with 'n' number of levels/floors and 'm' number of slots per level/floors
class ParkingLot:
	def __init__(self, noOfLevel, noOfSlot):
		self.level = []
		for i in range(noOfLevel):
			self.level.append(Level(i, noOfSlot))

	def ParkVehicle(self, vehicle):
		for level in self.level:
			if level.park(vehicle):
				return True
		return False

	def LeaveOperation(self, vehicle):
		for level in self.level:
			if level.remove(vehicle):
				return True

	def CompanyParked(self, companyName):
		vehicles = []
		for level in self.level:
			vehicles.extend(level.company(companyName))
		return vehicles
