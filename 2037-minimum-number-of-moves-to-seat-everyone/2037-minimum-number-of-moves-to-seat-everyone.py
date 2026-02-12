class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        # sorting both array to reduce the cost to move students
        sorted_seats = sorted(seats)
        sorted_student_pos = sorted(students)

        moves = 0

        for i in range(len(sorted_seats)):
            cost = abs(sorted_student_pos[i] - sorted_seats[i])

            if sorted_student_pos[i] < sorted_seats[i]:
                moves += cost
            else:
                moves += cost
        return moves