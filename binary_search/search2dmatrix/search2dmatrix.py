class Solution:

    def searchRow(self, matrix, target):
        low = 0
        high = len(matrix) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if matrix[mid][0] == target:
                return mid

            elif matrix[mid][0] > target:
                high = mid

            else:
                low = mid

        if matrix[high][0] < target:
            return high
        else:
            return low

    def searchMatrix(self, matrix, target):

        # boundary check
        if matrix is None or target is None:
            return False

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        insert_row = self.searchRow(matrix, target)
        row = matrix[insert_row]

        low = 0
        high = len(row) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if row[mid] == target:
                return True

            elif row[mid] < target:
                low = mid

            else:
                high = mid

        if row[low] == target:
            return True

        if row[high] == target:
            return True

        return False


if __name__ == '__main__':
    s = Solution()

    assert True == s.searchMatrix(
        matrix=[
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ],
        target=3
    )

    assert True == s.searchMatrix(
        matrix=[
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ],
        target=7
    )

    assert True == s.searchMatrix(
        [
            [1, 8, 15, 22, 29, 35, 37, 39, 44, 50, 57, 60, 61, 62, 69, 70, 71, 78, 80],
            [96, 113, 137, 150, 162, 183, 193, 203, 222, 243, 255, 279, 301, 312, 324, 344, 359, 381, 397],
            [407, 417, 428, 453, 469, 482, 498, 521, 537, 553, 564, 575, 592, 613, 634, 658, 675, 693, 714],
            [738, 761, 775, 785, 795, 812, 833, 850, 868, 890, 910, 934, 955, 966, 976, 996, 1014, 1037, 1052],
            [1073, 1085, 1096, 1121, 1135, 1159, 1182, 1196, 1210, 1221, 1241, 1262, 1279, 1298, 1318, 1330, 1347, 1365, 1386],
            [1398, 1423, 1444, 1459, 1483, 1507, 1517, 1528, 1542, 1558, 1568, 1583, 1605, 1630, 1641, 1651, 1665, 1690, 1714]
        ],
        80
    )

    assert True == s.searchMatrix(
        [
            [1, 2, 8, 10, 16, 21, 23, 30, 31, 37, 39, 43, 44, 46, 53, 59, 66, 68, 71],
            [90, 113, 125, 138, 157, 182, 207, 229, 242, 267, 289, 308, 331, 346, 370, 392, 415, 429, 440],
            [460, 478, 494, 506, 527, 549, 561, 586, 609, 629, 649, 665, 683, 704, 729, 747, 763, 786, 796],
            [808, 830, 844, 864, 889, 906, 928, 947, 962, 976, 998, 1016, 1037, 1058, 1080, 1093, 1111, 1136, 1157],
            [1180, 1204, 1220, 1235, 1251, 1272, 1286, 1298, 1320, 1338, 1362, 1378, 1402, 1416, 1441, 1456, 1475, 1488, 1513],
            [1533, 1548, 1563, 1586, 1609, 1634, 1656, 1667, 1681, 1706, 1731, 1746, 1760, 1778, 1794, 1815, 1830, 1846, 1861]
        ],
        1861
    )
