import math

cont_str = input("enter required contribution points: ")
cont = int(cont_str)
print(f"contribution required: {cont}!")

times = {
"disciple" : math.ceil((cont / 10))*10 + 0,
"deacon" : math.ceil((cont / 16))*10 + 10,
"Core Disciple" : math.ceil((cont / 24))*10 + 30,
"Supervisor" : math.ceil((cont / 36))*10 + 50,
"Guardian" :  math.ceil((cont / 56))*10 + 150,
"Elder" :  math.ceil((cont / 90))*10 + 300
}

for var_name, value in times.items():
    res = value / 60
    hours = int(res)
    minutes = int((res - hours)*60)
    print(f"Sect Title: {var_name}, Time: {hours} hrs {minutes} mins")
    
