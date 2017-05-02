from euler import NumberTriangle


if __name__ == '__main__':
    with open('p18_triangle.txt', 'r') as f:
        triangle = NumberTriangle(f.read().strip('\n'))

    for row in range(1, len(triangle[:])):
        for i in range(len(triangle[row])):
            bigger = max(triangle.right_parent(row, i),
                         triangle.left_parent(row, i))
            triangle[row][i] = triangle[row][i] + bigger
    print(max(triangle[len(triangle[:])-1]))
