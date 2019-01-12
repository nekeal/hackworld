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

$("#skills").multiSelect({
    selectableHeader: "<input type='text' class='search-input' autocomplete='off' placeholder='Start typing...'>"
});

$(".search-input").on("keyup", (e) => {
    console.log(e.currentTarget.value);
})