WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    times = int(size / 2)
    for row in range(times):
        print((WHITE + BLACK) * times)

create_chessboard(8)