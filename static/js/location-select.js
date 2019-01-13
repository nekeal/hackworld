
$("#location").on("keyup", (e) => {
    const city = e.currentTarget.value;

    if(city.length > 1) {
        $.get("/api/cities", { name: city })
        .done((cities) => {
            $("#cities").html(cities.map(city => `<option value="${city.name}">`).join(""));
        })
    }
})
