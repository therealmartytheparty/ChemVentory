import barcode
#can use either ean13 or ean8
#ean13 is for larger items becuase they larger sized
#ean8 is pretty small and can fit on smaller items
ean = barcode.get('ean13','123456891234')

ean.get_fullcode()

filename = ean.save('ean13')

filename
options = dict(compress=True)
filename = ean.save('ean13',options)
filename
