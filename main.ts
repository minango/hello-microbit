input.onButtonPressed(Button.A, function () {
    let スプライト: game.LedSprite = null
    basic.showIcon(IconNames.Heart)
    スプライト.turn(Direction.Right, 45)
})
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
        # # # . .
        . . . . .
        `)
    basic.showIcon(IconNames.Happy)
})
