c=int(input('Quantos kms você percorreu com o carro?'))
d=int(input('E quantos dias foi alugado?'))
vd=d*60
vc=c*0.15
vt=vc+vd
print('Você irá pagar por {}R$ pois percorreu por {} dias, e por {}R$ pois percorreu {}km e total irá parga{}R$'.format(vd,d,vc,c,vt))