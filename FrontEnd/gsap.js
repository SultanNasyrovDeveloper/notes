TweenMax.to(varialble, 3, {
    height: '10rem',
})

// special
var tween = TweenMax.from(smth, 5, {
    delay: 2,
    ease: Bounce.easeOut,
    paused: True, // animation will pause itself immediately upon creation.
    onComplete: myFunction,
    onStart: myFunction,
    repeat: 3,
    yoyo: True, //
    cycle: {
        x: [100, -100, 50, -50]
    }
})

// function-based views
TweenLite.to(".box", 1, {
  x: function() {
    return Math.random() * 300;
  }
});

// scrollTo
TweenMax.to(window, 3, {
    scrollTo: {
        y: '.some-class',
        ease: some,
        offsetY: 50,
        y:'max',

    },
})

// Timeline
//instantiate a TimelineLite
var tl = new TimelineMax();
    tl.to('selector', 0.7, {}, 0)


