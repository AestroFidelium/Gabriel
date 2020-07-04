maxHealth = 1000
Health = 100

Procent = (Health * 100) / maxHealth
WithOutProcent = 100 - Procent

Red = 2.55
Green = 200
Blue = 0

Red *= WithOutProcent
Green -= Red

print(f"\nХП : {Procent}%\n\nR:{Red}\nG:{Green}\nB:{Blue}")