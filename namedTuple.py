# (country_code, passeport_number)
from collections import namedtuple

traveler = [('USA','316665644'),('BRA','454654654154'),('ESP','45454654XS')]


city, year, pop, chg, area=('Tokyo', 2003, 32450, 0.66,8014)

lax_coordinates=(33.9425, -118.408056)
latitude, longitude=lax_coordinates

metro_areas=[('Tokyo','JP',36.9333,(35.565656,139.46565565)),
             ('Delhi NCR','IN',21.935,(28.226656,77.22266652)),
             ('Mexico City','MX',20.142,(19.43333,-99.2223665)),
             ('New York-Newark','US',20.104,(40.808611,-74.0233665)),
             ('Sao Paulo','BR',19.649,(-23.2222366,-46.233366)),]

City = namedtuple('City', 'name country population coordinates')

tokyo=City('tokyo','JP',36.933,(35.5646464,139.4664545))

LatLong = namedtuple('LatLong', 'lat long')

delhi_data = ('Delhi NCR','IN',21.935, LatLong(28.226656,77.22266652))

delhi = City._make(delhi_data)


