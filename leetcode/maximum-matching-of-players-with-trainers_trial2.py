class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # sorting the array
        players.sort()
        trainers.sort()

        first = 0
        second = 0

        count = 0

        
        while first < len(players) and second < len(trainers):
            if trainers[second] >= players[first]:
                count += 1

                first += 1
                second += 1
            else:
                second += 1

        return count