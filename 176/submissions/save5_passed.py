WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    w, b = WHITE, BLACK
    times = int(size / 2)
    for __ in range(size):
        print((w + b) * times)
        w, b = b, w
        

create_chessboard(2)