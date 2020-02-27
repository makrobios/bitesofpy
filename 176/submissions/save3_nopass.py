WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    w, b = WHITE, BLACK
    times = int(size / 2)
    for row in range(times):
        print((w + b) * times)
        w, b = b, w
        

