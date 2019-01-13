$("#skills").multiselect({});

$(".search-input").on("keydown", (e) => {
    const searchskill = e.currentTarget.value;
    console.log(searchskill);

    $.get("/api/skills", { name: searchskill })
    .done((skills) => {
        $("#skills").html(skills.map(skill => `<option value="${skill.id}">${skill.name}</option>`).join(""));
    })
})