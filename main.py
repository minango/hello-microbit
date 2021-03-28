def on_received_string(receivedString):
    music.play_melody(receivedString, 120)
radio.on_received_string(on_received_string)

basic.show_icon(IconNames.EIGTH_NOTE)
music.play_melody("C D E F G A B C5 ", 120)
radio.set_group(1)
radio.send_number(0)
radio.send_string("")

def on_forever():
    basic.show_leds("""
        . # # # .
        . . . # .
        . . # . .
        . . . # .
        . # # # .
        """)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . # .
        . . # . .
        # # # # #
        """)
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        . . # # .
        # # # . .
        . . # # #
        . . # . .
        # # # . .
        """)
    basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
