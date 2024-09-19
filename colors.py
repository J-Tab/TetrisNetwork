class Colors:
    red = (255,0,0)
    yellow = (255,255,51)
    purple = (127,0,255)
    green = (0,255,0)
    blue = (0,0,255)
    cyan = (0,255,255)
    dark_grey = (12,12,12)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey,cls.red,cls.yellow, cls.purple, cls.green, cls.blue, cls.cyan]