import {KeywordDict} from "keyworddict"
$(document).ready(function() {
    var dict = new KeywordDict();
    $.getJSON("data.json", function(data) {
        if (data.hasOwnProperty('companies')) {
            $.each(data.companies, function(name, values) {
                dict.put(name, name);
                $.each(values.keywords, function(index, keyword) {
                    dict.put(keyword, name);
                });
            });
        } else {
            console.log("could not load companies!");
        }
    });
});
