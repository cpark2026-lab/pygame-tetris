class Colors:
    dark_midnight = (18, 21, 26)      # deep midnight
    neon_mint = (0, 255, 180)         # neon mint
    neon_magenta_red = (255, 0, 110)           # neon magenta-red
    vivid_orange = (255, 140, 0)        # vivid orange
    bright_gold = (255, 215, 0)        # bright gold
    neon_violet = (120, 0, 255)        # neon violet
    electric_cyan = (0, 240, 255)          # electric cyan
    electric_blue = (0, 120, 255)          # electric blue

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_midnight, cls.neon_mint, cls.neon_magenta_red, cls.vivid_orange, cls.bright_gold, cls.neon_violet, cls.electric_cyan, cls.electric_blue]