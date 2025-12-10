def count_neighbours(grid,row_idx,col_idx):
    neighbours = 0
    for y in range(row_idx-1,row_idx+2):
        for x in range(col_idx-1,col_idx+2):
            if x < 0 or y < 0 or x >= len(grid[row_idx]) or y >= len(grid):
                continue
            if x == col_idx and y == row_idx:
                continue
            if grid[y][x]:
                neighbours += 1

    return neighbours

with open("./python/day-4/input.txt") as file:
    rows = [line.strip() for line in file.readlines()]

grid = []
for row_string in rows:
    row = []
    for cell_char in row_string:
        row.append(cell_char=="@")
    grid.append(row)

count = 0
items_removed = True

while items_removed:
    items_removed = False
    removed_items = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not grid[i][j]:
                continue
            if count_neighbours(grid,i,j) < 4:
                count += 1
                items_removed = True
                removed_items.append((i, j))
    
    for i, j in removed_items:
        grid[i][j] = False

print(count)