'''
Design and code a pricing engine that will be used to generate quotes for charterUP. Prices should be
computed using the following inputs: VehicleType, VehicleCount, PricingMethod, PricingMethodUnits, and
VehicleTypeRate.

price = VehicleCount * VehicelTypeRate * PricingMethod * PricingMethodUnits.


DESIGN ANSWER:

If i were to design the database,
I would put the type as the main key and pricing method : rate as the value;
An example of this would look like this

{VehicleType: {PricingMethod:Rate}}
This allows for easy access to the rate as long as we know the other two elements.

From the user we need an input of how many vehicles, vehicle type, vehicle rate, what pricemethod, and the units

Assume the database is passed as an argument 
or is something we can access

For now I just put is as an argument
We look up the rate using the vehicle type and the price method

Then we just mulitple the remaining elements to get our quote
VehicleCount * rate * Units


Since I have time, if i were to write this using a MySQl db, 
as the data looks in the sample code,
it would look as the 2nd following
'''

def quote(VehicleCount, VehicleType, VehiclePriceMethod, Units, db):
    rate = db[VehicleType][VehiclePriceMethod]
    return VehicleCount * rate * Units
        

#assume the database is called DB
import MySQLdb   
def quoteWithMySql(VehicleCount, VehicleType, VehiclePriceMethod, Units):
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()
    sql = "SELECT * FROM DB \
       WHERE VEHICLETYPE = '%s' \
       AND PRICEMETHOD = '%s'" % (VehicleType, VehiclePriceMethod)
    try:
        cursor.execute(sql)
        #there should only be one right element so fetchone should correct
        result = cursor.fetchone()
        #rate should be the 3rd element so we access it like this
        rate = result[2]
    except Exception:
        print( Exception )
        
    db.close()
    return VehicleCount * rate * Units
    