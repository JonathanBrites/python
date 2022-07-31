segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos)

dias = total_segs // 86400
segs_restantes1 = total_segs % 86400

horas = segs_restantes1 // 3600                   
segs_restantes2 = segs_restantes1 % 3600           

minutos = segs_restantes2 // 60               
segs_restantes_final = segs_restantes2 % 60   

print(dias,"dia(s),",horas,"hora(s),",minutos,"minuto(s) e",segs_restantes_final,"segundo(s).")