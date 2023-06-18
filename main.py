airportbeg = input("What is your origin?")
des = input("what is your destination? ")
cs = input("callsign :")
deptime = input("Departure time : ")
arrtime = input("estimated arrival time : ")
aircraft = input("Aircraft : ")
# Write Airport of origin
with open('origin.txt', 'w') as file:
    file.write(airportbeg+"-"+des)
# Write Airport of origin
with open('cs.txt', 'w') as file:
    file.write(cs)
# Write Airport of origin
with open('deptime.txt', 'w') as file:
    file.write(deptime)
# Write Airport of origin
with open('arrtime.txt', 'w') as file:
    file.write(arrtime)
# Write Airport of origin
with open('aircraft.txt', 'w') as file:
    file.write(aircraft)
