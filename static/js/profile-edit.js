let descriptionEdit = false;

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
    $(".user-skills-list").removeClass("block");
    $(".c-rating button").click((e) => {
        const value = $(e.currentTarget).text();
        const ratingElement = $(e.currentTarget).parent();
        ratingElement.attr("data-rating-value", value);
    })
});