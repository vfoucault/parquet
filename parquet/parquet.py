import random

from PIL import ImageDraw, Image

from .row import Row
from .lame import Lame

class Parquet(object):

    def __init__(self, width, length, lame_width=140, lames_length=[1200, 850, 500, 350]):
        self.width = width
        self.length = length
        self.lames = { 'width': lame_width, 'lengths': lames_length}

        # will be :
        #  { row_id: { item_no: Lame(x,y,z), ...}}
        self.parquet = {}
        self.current_row = 0
        self.max_rows = width / lame_width

        # #008cbb => bleu
        # #a0cb3c => vert
        # #af413d => rouge
        # #f5f276 => jaune
        # #f17238 => orange
        # #5a4269 => violet
        # #f9f6f2 => blanc
        # #ca4663 => rose
        self.cold_colors = ['#a0cb3c', '#f9f6f2', '#5a4269', '#008cbb']
        self.warm_colors = ['#f17238'] * 3 + ['#ca4663'] * 2 + ['#f5f276'] * 2
        self.colors = self.cold_colors + self.warm_colors
        self.im = Image.new('RGB', (width,length), (128,128,128))
        self.dr = ImageDraw.Draw(self.im)

    def get_my_xs(self, row):
        return self.lames['width'] * row.row_id, self.lames['width'] * row.row_id + self.lames['width']

    def draw_parquet(self):
        for row_id, row in self.parquet.iteritems():
            x, end_x = self.get_my_xs(row)
            for lame_id, lame in row.lames.iteritems():
                # print "x={}, end_x={}, y={}, end_y={}".format(x,end_x,lame.y, lame.end_y)
                # pprint(lame)
                self.dr.rectangle(((x, lame.y), (end_x, lame.end_y)), fill=lame.color, outline='black')

    def create_row(self):
        return Row(row_id=self.current_row, length=self.length, width=self.lames['width'])

    def get_a_lame(self, good_lengths, good_colors):
        color = random.choice(good_colors)
        length = random.choice(good_lengths)
        lame = Lame(length, self.lames['width'], color)
        return lame

    def add_row(self, row):
        self.parquet[row.row_id] = row
        self.current_row += 1

    def get_last_row(self):
        try:
            return self.parquet[max(self.parquet.keys())]
        except TypeError:
            return None
        except KeyError:
            return None
        except ValueError:
            return None

    def has_touching_colors(self, previous_row):
        pass


    def fill_parquet(self):
        while self.current_row <= self.max_rows:
            row = self.create_row()
            good_lenghts = list(self.lames['lengths'])
            good_colors = list(self.colors)
            while row.space_left > min(self.lames['lengths']):
                this_lame_good_lengths = list(good_lenghts)
                this_lame_good_colors = list(good_colors)
                previous_lame = row.get_last_lame()
                previous_row = self.get_last_row()
                if previous_lame:
                    this_lame_good_lengths.remove(previous_lame.length)
                    this_lame_good_colors.remove(previous_lame.color)
                if previous_row:
                    # now that i have row, let's find if there is a match with this y, or end_y except if item is item0
                    # get last row next Y
                    last_row_ys = [lame.y for lame_id, lame in previous_row.lames.iteritems()]
                    this_lame_good_lengths = [l for l in this_lame_good_lengths if not (row.y + l) in last_row_ys]
                    print "row={}, lame_id={}, ok_lenghts {}".format(row.row_id, row.get_next_lame_id(), this_lame_good_lengths)
                lame = self.get_a_lame(good_colors=this_lame_good_colors, good_lengths=this_lame_good_lengths)
                row.add_lame(lame)
            self.add_row(row)

    def show(self):
        self.im.show()


