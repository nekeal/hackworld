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
    const skill = e.currentTarget.value;

    $.get("/api/skills", { name: skill })
    .done((data) => {
        console.log(data);
    })
})

$("#city").on("keyup", (e) => {
    const city = e.currentTarget.value;

    $.get("/api/cities", { name: city })
    .done((data) => {
        console.log(data);
    })
})