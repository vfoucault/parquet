class Row(object):

    def __init__(self, row_id, length, width):
        self.row_id = row_id
        self.width = width
        self.length = length
        self.y = 0
        self.lames = {}
        self.space_left = length

    def check_space(self, lame):
        if lame.length + self.y > self.length:
            return False
        return True

    @property
    def num_lames(self):
        return len(self.lames.keys())

    def get_last_lame(self):
        try:
            return self.lames[max(self.lames.keys())]
        except ValueError:
            return None
        except TypeError:
            return None

    def get_next_lame_id(self):
        try:
            return max(self.lames.keys()) + 1
        except ValueError:
            return 0

    def add_lame(self, lame):
        # print "adding lame {}".format(lame)
        if self.check_space(lame):
            lame_id = self.get_next_lame_id()
            lame.y = self.y
            self.y = lame.end_y
            self.lames[lame_id] = lame
        self.space_left -= lame.length

    def del_lame(self, lame_id):
        del self.lames[lame_id]

    def __repr__(self):
        return "<Row row_id={} num_lames={}".format(self.row_id, self.num_lames)
