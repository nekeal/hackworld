$(".join-request").click((e) => {
    const teamId = $(e.currentTarget).data("id");

    $.post("/teams/join-request/", { "team-id": teamId })
    .done((data) => {
        console.log(data);
    })
});

$(".requests .accept").click((e) => {
    const teamId = $(e.currentTarget).parent().data("teamid");
    const userId = $(e.currentTarget).parent().data("userid");
    console.log(teamId, userId);

    $.post("/teams/join-request/", { "team-id": teamId, "user-id": userId, "accept": true})
    .done((data) => {
        console.log(data);
    })
});

$(".requests .decline").click((e) => {
    const teamId = $(e.currentTarget).parent().data("teamid");
    const userId = $(e.currentTarget).parent().data("userid");
    console.log(teamId, userId);

    $.post("/teams/join-request/", { "team-id": teamId, "user-id": userId ,"accept": false })
    .done((data) => {
        console.log(data);
    })
});