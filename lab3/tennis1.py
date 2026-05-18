class TennisGame1:
    
    PoinstsName = {0:"Love",1: "Fifteen",2:"Thirty",3:"Forty"}
    
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self._is_tie():
            return self._tie_score()
        
        if self._is_end_game():
            return self._end_game_score()
        
        return self._regular_game_score()
    
    def _is_tie(self):
        return self.p1points == self.p2points
    
    def _is_end_game(self):
        return self.p1points >=4 or self.p2points >=4
    
    def _tie_score(self):
        return{
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
    
    def _end_game_score(self):
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                return "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
            
    def _regular_game_score(self):
        p1_name = self.PoinstsName[self.p1points]
        p2_name = self.PoinstsName[self.p2points]
        return f"{p1_name}-{p2_name}"

    

