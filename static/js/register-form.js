let offset = 0;

$(".next-step").click((e) => {
    e.preventDefault();
    offset++;
    $(".step").css("transform", `translateX(-${offset*100}%)`);
});

$(".prev-step").click((e) => {
    e.preventDefault();
    offset--;
    $(".step").css("transform", `translateX(-${offset*100}%)`);
});

$(".step").css("transform", `translateX(-${offset*100}%)`);

