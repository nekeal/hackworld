let prevSkillInput = "";

$("#skills").multiselect({});

$(".search-input").on("keyup", (e) => {
    const skillInput = e.currentTarget.value;
    
    if(skillInput !== prevSkillInput) {
        prevSkillInput = skillInput;
        $("#skills").empty();
        $.get("/api/skills", { name: skillInput })
        .done((skills) => {
            $("#skills").html(skills.map(skill => `<option value="${skill.id}">${skill.name}</option>`).join(""));
        })
    }
})
