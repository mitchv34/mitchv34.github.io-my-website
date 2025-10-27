$(document).ready(function () {
  // add toggle functionality to award and bibtex buttons (abstract always shown)
  $("a.award").click(function () {
    $(this).parent().parent().find(".award.hidden").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open");
  });
  $("a.bibtex").click(function () {
    $(this).parent().parent().find(".award.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden").toggleClass("open");
  });
  $("a").removeClass("waves-effect waves-light");

  // bootstrap-toc
  if ($("#toc-sidebar").length) {
    // remove related publications years from the TOC
    $(".publications h2").each(function () {
      $(this).attr("data-toc-skip", "");
    });
    var navSelector = "#toc-sidebar";
    var $myNav = $(navSelector);
    Toc.init($myNav);
    $("body").scrollspy({
      target: navSelector,
    });
  }

  // add css to jupyter notebooks
  const cssLink = document.createElement("link");
  cssLink.href = "../css/jupyter.css";
  cssLink.rel = "stylesheet";
  cssLink.type = "text/css";

  let jupyterTheme = determineComputedTheme();

  $(".jupyter-notebook-iframe-container iframe").each(function () {
    $(this).contents().find("head").append(cssLink);

    if (jupyterTheme == "dark") {
      $(this).bind("load", function () {
        $(this).contents().find("body").attr({
          "data-jp-theme-light": "false",
          "data-jp-theme-name": "JupyterLab Dark",
        });
      });
    }
  });

  // trigger popovers
  $('[data-toggle="popover"]').popover({
    trigger: "hover",
  });

  // Ensure Bootstrap navbar toggle works properly
  $('.navbar-toggler').on('click', function() {
    var target = $($(this).data('target'));
    target.toggleClass('show');
    
    // Update button's aria-expanded attribute
    var expanded = target.hasClass('show');
    $(this).attr('aria-expanded', expanded);
  });

  // Handle dropdown clicks for mobile
  $('.dropdown-toggle').on('click', function(e) {
    if ($(window).width() < 992) { // Only on mobile
      e.preventDefault();
      var $dropdown = $(this).next('.dropdown-menu');
      $dropdown.toggleClass('show');
    }
  });

  // Close dropdown when clicking outside
  $(document).on('click', function(e) {
    if (!$(e.target).closest('.dropdown').length) {
      $('.dropdown-menu').removeClass('show');
    }
  });
});
