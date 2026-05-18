class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.points = {player1_name: 0, player2_name: 0}
        self.poinsts_name = {0:"Love",1: "Fifteen",2:"Thirty",3:"Forty"}
        

    def won_point(self, player_name):
        self.points[player_name] +=1

    def score(self):
        p1res = self.points[self.player1_name]
        p2res = self.points[self.player2_name]

        if self.is_tie(p1res,p2res):
            return "Deuce" if p1res>=3 else f"{self.poinsts_name[p1res]}-All"
        
        if self.is_end_game(p1res, p2res):
            return self.get_game_status(p1res,p2res)
        
        return f"{self.poinsts_name[p1res]}-{self.poinsts_name[p2res]}"
     

    def points_to_message(self,player):
        if(player == "player1"):
            return self.PoinstsName[self.p1_score]
        else:
            return self.PoinstsName[self.p2_score]

    def is_tie(self,points1,points2):
        return points1 == points2
    
    def is_end_game(self,points1,points2):
        return points1 >=4 or points2>=4
    
    def get_game_status(self,points1,points2):
        diff = points1 - points2
        leader = self.player1_name if diff > 0 else self.player2_name
        status = "Advantage" if abs(diff) == 1 else "Win for" 
        return f"{status} {leader}"
    
    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1
