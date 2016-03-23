import math

def get_cm(IP):
    IP_str = str(IP)       #in case it's not already str, convert to str
    IP_len = len(IP_str)   #get length of IP
    total_dist = 0         #initialize distance
    #create coordinate map
    coordinates = {'1':[0,1], '2':[1,1], '3':[2,1],
                   '4':[0,2], '5':[1,2], '6':[2,2],
                   '7':[0,3], '8':[1,3], '9':[2,3],
                   '.':[0,0], '0':[1,0], ' ':[2,0]
                   }
    
    for str_pos in range(IP_len):
        #if next position DNE, break out loop; str positions start at 0
        if (str_pos+1) == IP_len:
            break
        current_pos = coordinates[IP_str[str_pos]]
        diffX = current_pos[0] - coordinates[IP_str[str_pos+1]][0]
        diffY = current_pos[1] - coordinates[IP_str[str_pos+1]][1]
        total_dist += (math.sqrt(diffX**2 + diffY**2))
    
    #round distance to 2 decimal places
    total_dist = round(total_dist,2)
    
    return ('%.2fcm' % total_dist)
    