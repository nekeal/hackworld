function initMultiselect() {
    $("#skills").multiselect({});
}

let prevSkillInput = "";

$(".search-input").on("keyup", (e) => {
    const skillInput = e.currentTarget.value;
    
    if(skillInput !== prevSkillInput && skillInput !== "") {
        prevSkillInput = skillInput;
        $("#skills").empty();
        $.get("/api/skills", { name: skillInput })
        .done((skills) => {
            console.log(skills);
            $("#skills").html(skills.slice(0, 20).map(skill => `<option id="${skill.id}">${skill.name}</option>`).join(""));
        })
    }
})

function setSkill(e) {
    console.log(e);
}

function skillSearch(e) {
    const skillDatalist = $(e.currentTarget).next();
    const skillInput = e.currentTarget.value;

    console.log(skillDatalist);
    
    if(skillInput !== prevSkillInput && skillInput !== "") {
        prevSkillInput = skillInput;
        skillDatalist.empty();
        $.get("/api/skills", { name: skillInput })
        .done((skills) => {
            console.log(skills);
            skillDatalist.html(skills.slice(0, 20).map(skill => `<option onclick="setSkill(event)" data-id="${skill.id}">${skill.name}</option>`).join(""));
        })
    }
}
