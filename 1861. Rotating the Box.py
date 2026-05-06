# You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])
        
       
        for r in range(ROWS):
            empty_ptr = COLS - 1
            for c in range(COLS - 1, -1, -1):
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][empty_ptr] = ".", "#"
                    empty_ptr -= 1
                elif boxGrid[r][c] == "*":
                    empty_ptr = c - 1
                
        
        rotated_box = [["" for _ in range(ROWS)] for _ in range(COLS)]
        for r in range(ROWS):
            for c in range(COLS):
                rotated_box[c][ROWS - 1 - r] = boxGrid[r][c]
                
        return rotated_box
