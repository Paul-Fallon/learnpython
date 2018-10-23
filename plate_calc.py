

def platecalculator(weight, bar = 45,plates = [45,35,25,10,5,2.5]):
    net_weight = (weight-bar)/2.0
    required = {}
    for index, plate in enumerate(plates):
        required[plate] = net_weight//plate
        net_weight = net_weight-(plate*required[plate])
        
    return required

weight = 230

print(platecalculator(weight))

test = platecalculator(weight)

print(test[45])
