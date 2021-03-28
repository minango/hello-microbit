music.play_melody("C D E F G A B C5 ", 120)

def on_forever():
    basic.show_leds("""
        . # # # .
        . . . # .
        . . # . .
        . . . # .
        . # # # .
        """)
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . # .
        . . # . .
        # # # # #
        """)
basic.forever(on_forever2)

def on_forever3():
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
basic.forever(on_forever3)

def on_forever4():
    basic.show_leds("""
        . . # # .
        # # # . .
        . . # # #
        # # # . .
        . . . . .
        """)
basic.forever(on_forever4)
