# Parking-Lot

## Process Brief:

This is a Parking Lot system design using OOPs principle in python. The objects in the design are:
1. ParkingLot
2. Level
3. Slot
4. Vehicle

Below mentioned consideration has been made in the design: 
1. ParkingLot - A parking lot is made up of 'n' number of levels/floors and 'm' number of slots per floor.
2. Level - Each level is an independent entity with a floor number, its lanes and the slots within it. 
           The number of lanes are designed based on the number of slots. 10 slots make one lane
3. Slot - The slots are considered as the independent entities to each other where in the type of the vehicle is considered to fill the slot.
4. Vehicle - Object with plate no., company name and their type. A vehicle has the attributes of license plate and the company it is from.

Also,
1. Level and Slot are entities that are independent so that any level can be added with a desired number of slots later.
2. Each time a vehicle comes in or goes out, a list of vehicles for the particular company is updated.
3. The available slots are updated in the particular level.


Operation that can be performed:
1. ParkVehicle: This operation inserts a vehicle accordingly, also takes care of what company vehicle it is.
2. LeaveOperation - This operation exits a vehicle 'C' in a level 'm'.
3. CompanyParked - This operation allows the user to view the list of vehicles parked for a particular company.

