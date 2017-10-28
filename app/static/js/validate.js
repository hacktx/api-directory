// Wait for the DOM to be ready
$(function () {
    // Initialize form validation on the apis form.
    // It has the name attribute "apis-form"
    $("#apis-form").validate({
        ignore: ":not(:visible)",
        // Specify validation rules
        rules: {
            // The key name on the left side is the name attribute
            // of an input field. Validation rules are defined
            // on the right side
            company_name: "required",
            link: "required",
            image: "required",
            search_keywords: "required",
            chip_keywords: "required",
            description: "required"
        },
        // Specify validation error messages
        messages: {
            company_name: "Please enter the company's name",
            link: "Please enter the company's link",
            image: "Please enter the image directory path",
            search_keywords: "Please enter some search keywords",
            chip_keywords: "Please enter some chip keywords",
            description: "Please enter a description of the company"
        },
        errorPlacement: function (error, element) {
            if (element.hasClass("form-control")) {
                element.parent(".input-group").after(error);
            } else {
                element.after(error);
            }
            toastr['error']('Please fill out the required fields');
        }
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
    });


    // Initialize form validation on the apis form.
    // It has the name attribute "apis-form"
    $("#challenges-form").validate({
        ignore: ":not(:visible)",
        // Specify validation rules
        rules: {
            // The key name on the left side is the name attribute
            // of an input field. Validation rules are defined
            // on the right side
            company_name: "required",
            link: "required",
            image: "required",
            search_keywords: "required",
            chip_keywords: "required",
            prize_name: "required",
            prize: "required",

        },
        // Specify validation error messages
        messages: {
            company_name: "Please enter the company's name",
            link: "Please enter the company's link",
            image: "Please enter the image directory path",
            search_keywords: "Please enter some search keywords",
            chip_keywords: "Please enter some chip keywords",
            prize_name: "Please enter the prize's name",
            prize: "Please enter the prize",
        },
        errorPlacement: function (error, element) {
            if (element.hasClass("form-control")) {
                element.parent(".input-group").after(error);
            } else {
                element.after(error);
            }
            toastr['error']('Please fill out the required fields');
        }
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
    });
});
