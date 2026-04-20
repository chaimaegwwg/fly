from parsing import make_a_dictionary,check_hub
import re

#mission is make 2 array and display the place 
#mission tomorrow is for make sure for parsing also add attribuite like the cost 
#mission make sure u understand the dijikstra and do it 
# the finale parsing for the part of connection

class Grid:
    def __init__(self,name, row, col, zone=0, color =0, max_drones = 0):
        self.name = name 
        self.row = row
        self.col = col
        self.zone = zone
        self.color = color
        self.max_drones = max_drones
        self.place = 0


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
    grid[start_row][start_col].place = 1
    grid[end_row][end_col].name = "start_end"
    grid[end_row][end_col].place = 1
    for key , value in info.items():
        
        row , col =value["position"]
        row = int(row)
        col = int(col)
        name = value["name"]
        try:
            zone = value["zone"]
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
        grid[row][col].zone = zone
        grid[row][col].place = 1
        grid[row][col].name = name
        grid[row][col].color = color
        grid[row][col].max_drones = max_drone
    
    return grid
def main():
    dic = make_a_dictionary()
    position = []
    lst_position = []
    for key, value in dic.items():
        if key.strip() == "start_hub":
            for x in value:
                v = x.split()
                start = (int(v[1]),int(v[2]))
        if key.strip() == "end_hub":
            for x in value:
                v = x.split()
                end = (int(v[1]),int(v[2]))
    dic = make_a_dictionary()
    info,connection = check_hub(dic["hub"])
    grid = ft_info(info, start,end)
    display(grid,start, end)
    print(connection)

main()