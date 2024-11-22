polish_license_plates = [
   'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
   'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
   'KK54985', 'LU4864U'
]
counter = 0
for car_number in polish_license_plates:
   if car_number[0:2] == 'KR' or car_number[0:2] == 'KK':
      print(counter, polish_license_plates[polish_license_plates.index(car_number)])
      counter += 1