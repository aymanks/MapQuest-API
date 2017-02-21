#Ayman Syed, 87719684

#This module takes care of inputs, user interface

import mapquest_API_interact
import output_classes

def user_inputs(user_input: str) -> list:
    '''Takes user's inputs (number of locations)'''
    locations = []
    
    while True:
        num_of_locations = int(input())

        if user_input == str:
            if num_of_locations >= 2:
                break
        else:
            print('Please type in 2 or more locations.')
            
    for location in range(num_of_locations):
        locations.append(input())
    return locations

def user_outputs(user_output: str) -> list:
    '''Takes user outputs (number of outputs and a class)'''
    locations = []
    
    while True:
        num_of_locations = int(input())

        if user_output == str:
            if num_of_locations >= 1:
                break
            else:
                print('You need more outputs.')
                
    for location in range(num_of_locations):
        locations.append(input())
    return locations

def outputs(type_of_output: 'list of output', url):
    '''prints the output functions in the classes module'''
    for results in type_of_output:
        result = results.output(url)

def input_to_class(outputs: 'list of str') -> 'list of outputs':
    '''Changes inputs into desired outputs by using classes'''
    classes = []
    for output in outputs:
        if output == 'STEPS':
            classes.append(output_classes.STEPS())
        elif output == 'LATLONGS':
            classes.append(output_classes.LATLONG())
        elif output == 'TOTALDISTANCE':
            classes.append(output_classes.TOTAL_DISTANCE())
        elif output == 'TOTALTIME':
            classes.append(output_classes.TOTAL_TIME())
        elif output == 'ELEVATION':
            classes.append(output_classes.ELEVATION())
        else:
            print('Please type one of the following: STEPS, LATLONGS, TOTALDISTANCE, TOTALTIME, ELEVATION')
                  
    return classes

if __name__ == '__main__':
    route_query = user_inputs(str)
    OUTPUTS = user_outputs(str)
    URL = mapquest_API_interact.build_url(route_query)
    outputs(input_to_class(OUTPUTS), mapquest_API_interact.get_result(URL))
    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
