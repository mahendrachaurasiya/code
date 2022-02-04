amount=int(input())
while amount>=0:
    if(amount>=500):
       notes500=amount//500
       amount=amount-notes500*100
       print(notes500)
    elif amount>=100 :
       notes100=amount//100
       amount=amount-notes100*100
       print(notes100)
    elif amount>=50 :
       notes50=amount//50
       amount=amount-notes50*100
       print(notes50)
    elif amount>=20 :
       notes20=amount//20
       amount=amount-notes20*100
       print(notes20) 
    else:
       notes1=amount        



