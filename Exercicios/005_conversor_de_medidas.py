medida = float(input("Digite uma medida em metros para converter:"))

km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('MEDIDA CONVERTIDA')
print('Kilometros: {:.2f} km.'.format(km))
print('Hectometros: {:.2f} hm.'.format(hm))
print('Decâmetro: {:.2f} dam.'.format(dam))
print('Metros: {:.2f} m.'.format(m))
print('Decímetro: {:.2f} dm.'.format(dm))
print('Centímetro: {:.2f} cm.'.format(cm))
print('Milímetro: {:.2f} mm.'.format(mm))
