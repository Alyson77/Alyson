#缺少迷宫文件，只写了核心代码部分
class Maze:
    def __init__(self,mazeFilename):
        rowsInMaze=0
        columnsInMaze=0
        self.maselist=[]
        mazeFile=open(mazeFilename,'r')
        rowsInMaze=0
        for line in mazeFile:
            rowList=[]
            col=0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow=rowsInMaze
                    self.startCol=col
                col=col+1
            rowsInMaze=rowsInMaze+1
            self.maselist.append(rowList)
            columnsInMaze=len(rowList)

def searchFrom(maze,startRow,startColumn):
    maze.updatePosition(startRow,startColumn)
    if maze[startRow][startColumn] == OBSTACLE: #碰墙
        return False
    if maze[startRow][startColumn] == TRIED or \
        maze[startRow][startColumn] == DEAD_END: #碰面包屑或死胡同
        return False
    if maze.isExit(startRow,startColumn): #碰到出口
        maze.updatePosition(startRow,startColumn,PART_OF_PATH)
        return True
    maze.updatePosition(startRow,startColumn,TRIED) #洒面包屑
    found=searchFrom(maze,startRow-1,startColumn) or \
          searchFrom(maze,startRow+1,startColumn) or \
          searchFrom(maze,startRow,startColumn-1) or \
          searchFrom(maze,startRow,startColumn+1) #向北、南、西、东反向探索
    if found:
        maze.updatePosition(startRow,startColumn,PART_OF_PATH) #探索成功标记
    else:
        maze.updatePosition(startRow,startColumn,DEAD_END) #探索失败标记死胡同
    return found
