from datetime import datetime

class HistoricalData:
    def __init__(self, year: int, week: int, day: datetime, player: str, battlesdone: int, comments: str):
        self.year = year
        self.week = week
        self.day = day
        self.player = player
        self.battlesdone = battlesdone
        self.comments = comments

    def to_dict(self):
        """Converteix l'objecte a un diccionari per facilitar la serialització."""
        return {
            "year": self.year,
            "week": self.week,
            "day": self.day.isoformat() if self.day else None,
            "player": self.player,
            "battlesdone": self.battlesdone,
            "comments": self.comments
        }

    def __repr__(self):
        return (f"HistoricalData(year={self.year}, week={self.week}, day={self.day}, "
                f"player='{self.player}', battlesdone={self.battlesdone}, comments='{self.comments}')")
