let descriptionEdit = false;
let skillsEdit = false;

$("#description-edit").click(() => {
    if(!descriptionEdit) {
        $(".user-description form textarea").val($(".user-description .description").text().trim());
        $(".user-description .description").css("display", "none");
        $(".user-description form").css("display", "block");
    }
    else {
        $(".user-description .description").css("display", "block");
        $(".user-description form").css("display", "none");
    }
    descriptionEdit = !descriptionEdit;
});

$("#skills-edit").click(() => {
    if(!skillsEdit) {
        $(".c-rating button").click((e) => {
            setStarsHandler(e);
        })
    }
    else {
        $(".c-rating button").off("click");
    }
    $(".user-skills").toggleClass("editing");
    skillsEdit = !skillsEdit;
});

$("#skills-send").click(() => {
    const prefix = "participantskill_set-";

    const data = {};

    const total = $(".user-skill").length, initial = total - $(".user-skill-new").length;

    data[prefix + "TOTAL_FORMS"] = total;
    data[prefix + "INITIAL_FORMS"] = initial;
    data[prefix + "MIN_NUM_FORMS"] = 0;
    data[prefix + "MAX_NUM_FORMS"] = 1000;

    $(".user-skill").each((index, skill) => {
        if(!$(skill).hasClass("user-skill-new")) {
            data[prefix + index + "-skill"] = $(skill).find(".name").data("id");
            data[prefix + index + "-id"] = $(skill).data("id");
        }
        else {
            data[prefix + index + "-skill"] = $(skill).find("datalist option").data("id");
        }
        data[prefix + index + "-advanced_level"] = $(skill).find(".c-rating").data("rating-value");
        if($(skill).hasClass("user-skill-remove")) {
            data[prefix + index + "-DELETE"] = "on";
        }
        data[prefix + index + "-participant"] = $(".user-details").data("id");
    });

    console.log(data);

    $.post("/profile/skills/", data)
    .done(data => {
        location.reload();
    }) 

});

function setStarsHandler(e) {
    const value = $(e.currentTarget).text();
    const ratingElement = $(e.currentTarget).parent();
    ratingElement.attr("data-rating-value", value);
}

let counter = 0;

$(".user-skills .add").click((e) => {
    const newRecord = `
        <div class="user-skill user-skill-new">
            <input onkeyup="skillSearch(event)" type="text" list="skills${counter}">
            <datalist id="skills${counter}"></datalist>
            <div class="c-rating c-rating--big" data-rating-value="0">
                <button>1</button>
                <button>2</button>
                <button>3</button>
                <button>4</button>
                <button>5</button>
            </div>
        </div>
    `;

    counter++;
    $(newRecord).insertBefore(e.currentTarget);
    $(".c-rating button").click((e) => {
        setStarsHandler(e);
    })
})

$(".user-skills .remove").click((e) => {
    $(e.currentTarget).parent().addClass("user-skill-remove")
})