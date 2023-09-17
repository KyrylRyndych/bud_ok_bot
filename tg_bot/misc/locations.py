class Point():
    def __init__(self, lat, long) -> None:
        self.latitude = lat
        self.longitude = long


truskav = Point(49.797625, 24.011280 )
zelena  = Point(49.8120419374225, 24.061463338369506)

location = {"truskav" : truskav,
            "zelena": zelena}
pass