magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud >1 and magnitud <2:  # 1 <= magnitud <2:  #  cualquiera de las dos formas es la correcta pero esta opción comentada lo hace mas practico.
    print("Not felt or rarely felt")
elif magnitud >=2 and magnitud <4:   # 2 <= magnitud <4:   
    print("Very rarely causea damages")
elif 4 <= magnitud <5:
    print("Damage to weak buildings")
elif 5 <= magnitud <6:
    print("Damage only poor constructed buildings")
elif 6 <= magnitud <7:
    print("Damage good constucted buildings")
elif 7 <= magnitud <8:
    print("Causes damage to almost all buildings")
elif 8 <= magnitud <9:
    print("Causes major destruction")
elif magnitud >=9:
    print("Causes ubelievable damage")
else:
    print("Magnitude not found.")


