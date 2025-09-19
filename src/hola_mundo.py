from datetime import datetime

hora_actual = datetime.now().hour
NOMBRE=input("Escribe tu nombre")
if(hora_actual<12):
    print(f"¡Buenos días, {NOMBRE}!")
if(12<=hora_actual<20):
    print(f"¡Buenas tardes, {NOMBRE}!")
if(20<=hora_actual<23):
    print(f"¡Buenas noches, {NOMBRE}!")
