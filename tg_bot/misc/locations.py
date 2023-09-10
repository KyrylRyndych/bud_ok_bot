class Point():
    def __init__(self) -> None:
        self.latitude = None
        self.longitude = None


truskav = Point()
truskav.latitude = 49.797625
truskav.longitude = 24.011280

zelena  = Point()
zelena.latitude = 49.8120419374225
zelena.longitude = 24.061463338369506


location = {"truskav" : truskav,
            "zelena": zelena}
pass