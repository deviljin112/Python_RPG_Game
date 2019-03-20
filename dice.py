from random import randint
from math import sqrt, ceil

class Die:
    def __init__(self, faces_count, eyes='o ', corner='+'):

        if len(eyes) != 2:
            raise ValueError('Expected two choices for eyes parameter')

        self.eyes = eyes
        width = int(sqrt(faces_count))
        height = ceil(faces_count/width)

        while height > width + 1:
            width += 1
            height = ceil(faces_count/width)

        height = int(height)
        if not height % 2:
            height += 1

        self.limit = width * height
        self.faces = faces_count

        pattern = ' '.join('{}' for _ in range(width))
        pattern = '| {} |'.format(pattern)
        top = corner + ('-' * (2 * width + 1)) + corner
        middle = ' '.join('{}' for _ in range(width//2))
        middle = '| ' + middle + ' ' * (width % 2)
        self.pattern = '\n'.join([top] + [pattern for _ in range(height//2)] + [middle])

        self.width = len(top)
        self.height = self.pattern.count('\n') * 2 + 1


    def face(self, roll):

        if not (0 <= roll < self.faces):
            raise ValueError('Roll is higher than die size or negative')

        eye_full, eye_empty = self.eyes

        upper_face = self.pattern.format(*(eye_empty if roll < i else eye_full
            for i in range(1, self.limit, 2)))

        return upper_face + self.eyes[roll&1] + upper_face[::-1]


def dice_rolls(faces_count, number_of_rolls):

    return [randint(1, faces_count) for _ in range(number_of_rolls)]


def print_dice_rolls(faces_count, rolls, zero_based=False,  max_width=72, eyes='o '):

    print('\n{}'.format(rolls), "\n")

    die = Die(faces_count, eyes)
    face_width = die.width

    output_buffer = ['' for _ in range(die.height)] 

    for roll in (r + zero_based - 1 for r in rolls):

        if len(output_buffer[0]) + face_width >= max_width:
            for idx, line in enumerate(output_buffer):
                print(line)
                output_buffer[idx] = ''

        current_face = die.face(roll)

        for idx, line in enumerate(current_face.split('\n')):
            output_buffer[idx] += line + '  '

    if output_buffer[0]:
        for line in output_buffer:
            print(line)