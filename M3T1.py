# CTI-110
# M3T1 - Area of Triangle
# Gardner
# 09/13/2017

#calc first Triangle
firstWidth = int(input('width of first?'))
firstLength = int(input('length of first?'))

secondWidth = int(input('width of second?'))
secondLength = int(input('length of second?'))
#calc area
firstArea = firstWidth * firstLength
print('first area is', firstArea,)
secondArea = secondWidth * secondLength
print('second area is', secondArea,)
#prgrm Logic
if firstArea > secondArea:
    print('first has larger area')
else:
    if firstArea < secondArea:
        print('second has larger area')
if firstArea == secondArea:
    print('both have equal area')
print('done')

        
            
