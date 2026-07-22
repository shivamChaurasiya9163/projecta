/*=========================================
    SGenovix Technologies
    Infinite Portfolio Slider
==========================================*/

document.addEventListener("DOMContentLoaded", () => {

    const track = document.querySelector(".slider-track");
    const prevBtn = document.querySelector(".prev");
    const nextBtn = document.querySelector(".next");

    if (!track) return;

    let cards = Array.from(track.children);

    const gap = 30;

    // Clone first and last cards

    const firstClone = cards[0].cloneNode(true);
    const lastClone = cards[cards.length - 1].cloneNode(true);

    firstClone.classList.add("clone");
    lastClone.classList.add("clone");

    track.appendChild(firstClone);
    track.insertBefore(lastClone, cards[0]);

    cards = Array.from(track.children);

    let index = 1;

    let cardWidth;

    function updateCardWidth() {

        cardWidth = cards[index].offsetWidth + gap;

    }

    updateCardWidth();

    window.addEventListener("resize", () => {

        updateCardWidth();

        moveSlider(false);

    });

    function moveSlider(animation = true) {

        if (animation) {

            track.style.transition = "transform .6s ease";

        } else {

            track.style.transition = "none";

        }

        track.style.transform =
            `translateX(-${index * cardWidth}px)`;

    }

    moveSlider(false);

    nextBtn.addEventListener("click", nextSlide);

    prevBtn.addEventListener("click", prevSlide);

    function nextSlide() {

        if (index >= cards.length - 1) return;

        index++;

        moveSlider();

    }

    function prevSlide() {

        if (index <= 0) return;

        index--;

        moveSlider();

    }

    track.addEventListener("transitionend", () => {

        if (cards[index].classList.contains("clone")) {

            track.style.transition = "none";

            if (index === cards.length - 1) {

                index = 1;

            }

            if (index === 0) {

                index = cards.length - 2;

            }

            track.style.transform =
                `translateX(-${index * cardWidth}px)`;

        }

    });

    /*==========================
        Auto Play
    ==========================*/

    let autoPlay = setInterval(nextSlide, 3500);

    function stopAuto() {

        clearInterval(autoPlay);

    }

    function startAuto() {

        clearInterval(autoPlay);

        autoPlay = setInterval(nextSlide, 3500);

    }

    track.addEventListener("mouseenter", stopAuto);

    track.addEventListener("mouseleave", startAuto);
        /*==========================
        Mouse Drag
    ==========================*/

    let isDragging = false;
    let startPosition = 0;
    let currentTranslate = 0;
    let previousTranslate = 0;

    function getPositionX(event) {

        return event.type.includes("mouse")
            ? event.pageX
            : event.touches[0].clientX;

    }

    function dragStart(event) {

        stopAuto();

        isDragging = true;

        startPosition = getPositionX(event);

        previousTranslate = -index * cardWidth;

        track.style.transition = "none";

        track.classList.add("dragging");

    }

    function drag(event) {

        if (!isDragging) return;

        const currentPosition = getPositionX(event);

        currentTranslate =
            previousTranslate + (currentPosition - startPosition);

        track.style.transform =
            `translateX(${currentTranslate}px)`;

    }

    function dragEnd() {

        if (!isDragging) return;

        isDragging = false;

        track.classList.remove("dragging");

        const movedBy = currentTranslate - previousTranslate;

        if (movedBy < -80) {

            index++;

        } else if (movedBy > 80) {

            index--;

        }

        moveSlider();

        startAuto();

    }

    track.addEventListener("mousedown", dragStart);
    track.addEventListener("mousemove", drag);
    track.addEventListener("mouseup", dragEnd);
    track.addEventListener("mouseleave", dragEnd);

    track.addEventListener("touchstart", dragStart, {
        passive: true
    });

    track.addEventListener("touchmove", drag, {
        passive: true
    });

    track.addEventListener("touchend", dragEnd);

    /*==========================
        Keyboard Support
    ==========================*/

    document.addEventListener("keydown", (e) => {

        if (e.key === "ArrowRight") {

            nextSlide();

        }

        if (e.key === "ArrowLeft") {

            prevSlide();

        }

    });

});