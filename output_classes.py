#Ayman Syed, 87719684

#This module takes care of the output classes (STEPS, LATLONG, TOTALTIME,
#TOTALDISTANCE, ELEVATION)

class STEPS:
    '''class for step-by-step directions, a brief description of each
    maneuver you would have to make to drive from one location to another'''
    def output(self, json):
        print('DIRECTIONS')
        for place in json['route']['legs']:
            for route in place['maneuvers']:
                print(route['narrative'])
        print()       

class LATLONG:
    '''class for the latitude and longitude of each location specified
    in trip'''
    def output(self, json):
        print('LATLONGS')
        for place in json['route']['locations']:
            long = place['displayLatLng']['lng']
            lat = place['displayLatLng']['lat']

        if lat >= 0:
            print('{}N'.format(float(round(lat, 2))))
        else:
            print('{}S'.format(float(round(lat, 2))))

        if long >= 0:
            print('{}E'.format(float(round(long, 2))))
        else:
            print('{}W'.format(float(round(long, 2))))
        print()

class TOTAL_DISTANCE:
    '''class for total distance traveled if completing the entire trip'''
    def output(self, json):
        print('TOTAL DISTANCE: ' + str(int(json['route']['distance'])) + ' miles')
        print()
        
class TOTAL_TIME:
    '''class for the total estimated time to complete entire trip'''
    def output(self, json):
        time = str(int(round((json['route']['time'])) / 60))
        print('TOTAL TIME: ' + time + ' minutes')
        print()
        
class ELEVATION:
    '''class for the elevation, in feet, of each location specfied in input'''
    def output(self, json):
        print('ELEVATIONS')
        for place in json['route']['locations']:
            print(str(int(round(place['displayLatLng']['lat']))))
        print()
