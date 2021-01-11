while True:
    basic.show_leds("""
    . # . # .
    # # # # #
    # # # # #
    . # # # .
    . . # . .
    """)
    control.wait_micros(4)
    basic.show_leds("""
    . # . # .
    # . # . #
    # . . . #
    . # . # .
    . . # . .
    """)
