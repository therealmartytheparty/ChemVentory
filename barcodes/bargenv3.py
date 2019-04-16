import barcode
#can use various barcodes
#ean13 is for larger items becuase they larger sized
#ean8 is pretty small and can fit on smaller items
num_in= str(input("Type in a number to make a barcode from it"))

print(num_in)
var = "000000"+num_in+"0"

ean = barcode.get('ean8',var)

ean.get_fullcode()

filename = ean.save(var)

filename
options = dict(compress=True)
filename = ean.save(var,options)
filename
