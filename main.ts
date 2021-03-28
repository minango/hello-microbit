basic.showIcon(IconNames.EigthNote)
music.playMelody("C D E F G A B C5 ", 120)
basic.forever(function () {
    basic.showLeds(`
        . # # # .
        . . . # .
        . . # . .
        . . . # .
        . # # # .
        `)
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . # .
        . . # . .
        # # # # #
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.showLeds(`
        . . # # .
        # # # . .
        . . # # #
        . . # . .
        # # # . .
        `)
})
