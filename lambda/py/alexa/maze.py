import uuid
from . import data


class Maze:
    def __init__(self, maze_data=None, floor=None):
        if not maze_data:
            # mazes = [self.simple_maze, self.maze_1, self.maze_2]
            # if not floor:
            #     floor = 0
            # mazes[floor]()

            maze_data = {
                'rooms': data.MAZE_OF_FLOOR[floor],
                'cur_room': data.MAZE_OF_FLOOR[floor]['0']
            }

        self.rooms = {}
        for room_id, room in maze_data['rooms'].items():
            self.rooms[room_id] = Room(room_data=room)
        self.cur_room = Room(room_data=maze_data['cur_room'])

    def maze_1(self):
        r0, r1, r2, r3, r4, rb = Room(), Room(), Room(), Room(), Room(), Room()
        r0.id, r1.id, r2.id, r3.id, r4.id, rb.id = (
            '0', '1', '2', '3', '4', 'boss')
        r0.north = r2.id
        r0.room_type = 'VISITED'
        r1.north = r4.id
        r1.east = r2.id
        r1.room_type = 'HEAL'
        r2.west = r1.id
        r2.south = r0.id
        r2.north = r4.id
        r2.east = r3.id
        r2.room_type = 'ATTUP'
        r3.west = r2.id
        r3.north = r4.id
        r3.room_type = 'POISON'
        r4.west = r1.id
        r4.south = r2.id
        r4.east = r3.id
        r4.north = rb.id
        rb.south = r4.id
        rb.room_type = 'BOSS'
        self.rooms = {r0.id: r0, r1.id: r1, r2.id: r2,
                      r3.id: r3, r4.id: r4, rb.id: rb}
        self.cur_room = r0

    def maze_2(self):
        r0, r1, r2, r3, r4, r5, r6, rb = Room(), Room(
        ), Room(), Room(), Room(), Room(), Room(), Room()
        r0.id, r1.id, r2.id, r3.id, r4.id, r5.id, r6.id, rb.id = (
            '0', '1', '2', '3', '4', '5', '6', 'boss')
        r0.north = r1.id
        r0.west = r2.id
        r0.east = r3.id
        r0.room_type = 'VISITED'
        r1.south = r0.id
        r1.room_type = 'ATTDOWN'
        r2.south = r0.id
        r2.north = r4.id
        r2.room_type = 'ATTUP'
        r3.south = r0.id
        r3.north = rb.id
        r3.room_type = 'DEFUP'
        r4.north = r5.id
        r4.south = r2.id
        r4.east = rb.id
        r4.west = r6.id
        r5.south = r4.id
        r5.room_type = 'HEAL'
        r6.east = r4.id
        r6.room_type = 'DEFDOWN'
        rb.west = r4.id
        rb.south = r3.id
        rb.room_type = 'BOSS'
        self.rooms = {r0.id: r0, r1.id: r1, r2.id: r2, r3.id: r3,
                      r4.id: r4, r5.id: r5, r6.id: r6, rb.id: rb}
        self.cur_room = r0

    def simple_maze(self):
        r0, rb = Room(), Room()
        r0.id, rb.id = ('0', 'boss')
        r0.east = rb.id
        r0.room_type = 'VISITED'
        rb.west = r0.id
        self.rooms = {r0.id: r0, rb.id: rb}
        self.cur_room = r0

    def to_dict(self):
        rooms_dict = {}
        for room in self.rooms.values():
            rooms_dict[room.id] = room.to_dict()
        ret = {'cur_room': self.cur_room.to_dict(), 'rooms': rooms_dict}
        return ret


class Room:
    def __init__(self, room_data=None, north=None, south=None, west=None, east=None, room_type=None):
        if not room_data:
            self.id = uuid.uuid4().hex
            self.north = north
            self.south = south
            self.west = west
            self.east = east
            self.room_type = room_type
            self.is_marked = False
        else:
            self.from_dict(room_data)

    def mark(self):
        self.is_marked = True
        self.room_type = 'VISITED'

    def to_dict(self):
        ret = {}
        ret['id'] = self.id
        ret['north'] = self.north
        ret['south'] = self.south
        ret['west'] = self.west
        ret['east'] = self.east
        ret['room_type'] = self.room_type
        ret['is_marked'] = self.is_marked

        return ret

    def from_dict(self, room_data):
        self.id = room_data['id']
        self.north = room_data['north']
        self.south = room_data['south']
        self.west = room_data['west']
        self.east = room_data['east']
        self.room_type = room_data['room_type']
        if 'is_marked' in room_data:
            self.is_marked = room_data['is_marked']
        else:
            self.is_marked = False
