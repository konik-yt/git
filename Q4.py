sensor_readings1 = [10,23,None,"232.23",1.23]
sensor_readings2 = [20,"wow","crazy","W","Temp",None,200]

def clean_readings(lst):
    clean = []
    rejected = 0
    for i in range(len(lst)):
        clean.append(0)
    for i in range(len(lst)):
        try:
            clean[i] = float(lst[i])
        except ValueError:
            clean[i] = 0
            rejected +=1
        except TypeError:
            clean[i] = 0
            rejected +=1
    for i in range(len(clean)):
        if clean[i] >= 0 and clean[i] < 100:
            clean[i] = clean[i]
        else:
            clean[i] = 0
            rejected +=1
    for i in range(len(clean)):
        if 0 in clean:
            clean.remove(0)
        else:
            break
    return clean,min(clean),max(clean),sum(clean)/len(clean),rejected


print(clean_readings(sensor_readings1))
print(clean_readings(sensor_readings2))