$(function () {
  // slide 2
  $("#jq-btn").on("click", function () {
    $("#compare").text("Changed with jQuery");
  });

  // slide 4 - tag, class, id
  $("#select-btn").on("click", function () {
    $("p").css("font-weight", "bold");
    $(".fruit").css("color", "green");
    $("#title").css("color", "blue");
  });

  // slide 5
  $("#click-btn").on("click", function () {
    $(this).text("Clicked!");
  });

  $("#name").on("keyup", function () {
    $("#greeting").text("Hello " + $(this).val());
  });

  // slide 6
  $("#add-btn").on("click", function () {
    $("#list").append("<li>New item</li>");
  });

  $("#remove-btn").on("click", function () {
    $("#list li").last().remove();
  });

  // slide 7
  $("#color-btn").on("click", function () {
    $("#box").css("background-color", "orange");
  });

  $("#toggle-btn").on("click", function () {
    $("#box").toggleClass("rounded");
  });
});
