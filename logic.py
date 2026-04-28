from parsing import make_a_dictionary,check_hub
import re

#mission is make 2 array and display the place 
#mission tomorrow is for make sure for parsing also add attribuite like the cost 
#mission make sure u understand the dijikstra and do it 
# the finale parsing for the part of connection

class Grid:
    def __init__(self,name, row, col, zone=0, color =0, max_drones = 0,visited=0,value=0):
        self.name = name 
        self.row = row
        self.col = col
        self.zone = zone
        self.color = color
        self.max_drones = max_drones
        self.place = 0
        self.value = 0
        self.visited = False

def display(grid, start , end):
    start_row, start_col = start
    end_row, end_col = end
    end_col = end_col+1
    end_row = end_row+1
    for x in range(start_row, end_row):
        for y in range(start_col, end_col):
            if grid[x][y].place == 1:
                print(" + ",end="")
            else:
                print(" - ",end="")
            
        print()
    
def ft_info(info, start,end):
    start_row, start_col = start 
    end_row ,end_col = end
    row_list = []
    grid = []
    end_r = end_row +1
    end_c = end_col+1
    check = 0
    for x in range(start_row, end_r):
        row_list = []
        for y in range(start_col, end_c):
            step = Grid("anonymous",x,y)
            row_list.append(step)
        grid.append(row_list)
  
    grid[start_row][start_col].name = "start_hub"
    grid[start_row][start_col].place = 0
    grid[end_row][end_col].name = "start_end"
    grid[end_row][end_col].place = 5
    grid[end_row][end_col].zone = 5
    
    for key , value in info.items():
        row , col =value["position"]
        row = int(row)
        col = int(col)
        name = value["name"]
            
        try:
            zone = value["zone"]
            if zone == "priority":
                zone = 1
            elif zone == "normal":
                zone = 5
            elif zone == "restricted":
                zone = 20
            elif zone == "first":
                zone = 0
            else:
                zone = None
        except:
            zone = 0
        try:
            max_drone = value["max_drones"]
            max_drone = int(max_drone)
        except:
            max_drone = 0
        try:
            color = value["color"]
        except:
            color = 0
        # if value["name"] == "goal":
        #     grid[row][col].zone = 5
        grid[row][col].zone = zone
        grid[row][col].visited = False
        grid[row][col].place = 1
        grid[row][col].name = name
        grid[row][col].color = color
        grid[row][col].max_drones = max_drone
    
    return grid
# def zone_cost(zone):
#     if zone == "priority":
#         zone = 1
#     elif zone == "normal":
#         zone = 5
#     elif zone == "restricted":
#         zone = 20
#     else:
#         zone = None

def choice_the_path(places,info,grid,visited):
    dic = {}
    zone = float('inf')
    for i in places:
        if i in visited:
            continue
        place,v = i
        row ,col= info[place]["position"]
        row = int(row)
        col = int(col)
        dic[grid[row][col].name] = grid[row][col].zone
        if grid[row][col].visited:
            continue
        if zone > grid[row][col].zone:
            zone = grid[row][col].zone
            name = place
        
    
    return name,zone,dic
        

def chose_min(dic,visited,val):
    print("visited",visited)
    print(dic)
    x = float('inf')
    dic = dict(dic)
    for key,value in dic.items():
        value = int(value)
        if key in visited:
            continue
        if value+val < x and not key in visited:
            x = value
            name = key
    return name , value

    
def dijikstra(connection, info,grid):
    place = next(iter(connection))
    visited = []
    visited.append(place)
    value = 0
    dic_all = {}
    n = 0
    while True:
        dic = {}
        row ,col= info[place]["position"]
        row = int(row)
        col = int(col)
        if not grid[row][col].visited:
            grid[row][col].value = value
            grid[row][col].visited =True
        name ,v,dic = choice_the_path(connection[place],info,grid,visited)
        place, v = chose_min(dic,visited,value)
        print("here value",v)
        if not name in dic_all:
            dic_all[name] = []
        dic_all[name].append(dic)
        visited.append(place)
        print(place)
        value += v
        print("value",value)
        n +=1
        if n == 3:
            break






def main():
    dic = make_a_dictionary()
    position = []
    lst_position = []
    for key, value in dic.items():
        if key.strip() == "start_hub":
            for x in value:
                v = x.split()
                start = (int(v[1]),int(v[2]))
                v = start
        if key.strip() == "end_hub":
            for x in value:
                d = x.split()
                end = (int(d[1]),int(d[2]))
                d = end 
    dic = make_a_dictionary()
    # return end,start
    info,connection = check_hub(dic["hub"])
    info["hub"] = {"name": "hub", "position": v, "zone": "first", "max_drones": dic["nb_drones"]}
    info["goal"] = {"name": "goal", "position": d, "zone": "normal", "max_drones": dic["nb_drones"]}
    # print(info)
    grid = ft_info(info, start,end)
    dijikstra(connection,info,grid)

main()