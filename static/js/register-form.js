let offset = 2;

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

$("#skills").multiselect({});

$(".search-input").on("keyup", (e) => {
    const searchskill = e.currentTarget.value;
    console.log(searchskill);

    $.get("/api/skills", { name: searchskill })
    .done((skills) => {
        $("#skills").html(skills.map(skill => `<option value="${skill.id}">${skill.name}</option>`).join(""));
    })
})

$("#location").on("keyup", (e) => {
    const city = e.currentTarget.value;

    if(city.length > 2) {
        $.get("/api/cities", { name: city })
        .done((cities) => {
            $("#cities").html(cities.map(city => `<option value="${city.name}">`).join(""));
        })
    }
})