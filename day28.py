# LeetCode 1861 - Rotating the Box
# User Input and Output Version

def rotateTheBox(boxGrid):
    rows = len(boxGrid)
    cols = len(boxGrid[0])

    # Step 1: Simulate gravity for each row
    for r in range(rows):
        empty = cols - 1

        for c in range(cols - 1, -1, -1):

            if boxGrid[r][c] == '*':
                empty = c - 1

            elif boxGrid[r][c] == '#':
                boxGrid[r][c] = '.'
                boxGrid[r][empty] = '#'
                empty -= 1

    # Step 2: Rotate the box 90 degrees clockwise
    result = [[''] * rows for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            result[c][rows - 1 - r] = boxGrid[r][c]

    return result


# -------- USER INPUT --------

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter the box grid row by row")
print("Use # for stone, * for obstacle, . for empty")

boxGrid = []

for i in range(m):
    row = list(input(f"Row {i+1}: ").split())
    boxGrid.append(row)

# -------- FUNCTION CALL --------

answer = rotateTheBox(boxGrid)

# -------- OUTPUT --------

print("\nRotated Box Output:")

for row in answer:
    print(row)
