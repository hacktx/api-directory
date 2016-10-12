function put(key, value) {
    var list = sessionStorage.getItem(key);
    if (list) {
        sessionStorage.setItem(key, list.includes(value) ? list : list + " " + value);
    } else {
        sessionStorage.setItem(key, value);
    }
}

function get(key) {
    var list = sessionStorage.getItem(key);
    return list ? new Set(list.split(" ")) : new Set();
}

var $loadJSONPromise;
if (sessionStorage.getItem("done")) {
    $loadJSONPromise = $.Deferred().resolve();
} else {
    sessionStorage.clear();
    $loadJSONPromise = $.getJSON("/data.json", function(data) {
        if (data.hasOwnProperty('companies')) {
            $.each(data.companies, function(name, values) {
                put(name.toLowerCase(), name.toLowerCase());
                $.each(values.keywords, function(index, keyword) {
                    put(keyword.toLowerCase(), name.toLowerCase());
                });
            });
        }
        sessionStorage.setItem("done", "true");
    });
}

$(document).ready(function() {
    // show or hide appropriate elements
    var query = window.location.search;
    var $cards = $(".api-card-div");

    function parseQuery(query) {
        if (!query || query.charAt(0) !== '?') {
            return null;
        }
        query = query.substring(1);
        // convert GET request to JSON and parse params. Code copied from
        // https://stackoverflow.com/questions/8648892/convert-url-parameters-to-a-javascript-object
        var queryParams = JSON.parse('{"' + decodeURI(query).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g,'":"').replace(/\+/g, " ") + '"}');
        if (!queryParams.hasOwnProperty('query')) {
            return null;
        }
        return queryParams['query'];
    }

    function runQuery(query) {
        var apiSet = null;
        if (query) {
            var wordSet = new Set(query.toLowerCase().split(" "));
            wordSet.forEach(function(word) {
                var queryResults = get(word);
                if (apiSet === null) {
                    apiSet = new Set(queryResults);
                } else if (apiSet.size > 0) {
                    apiSet.forEach(function(api) {
                        if (!queryResults.has(api)) {
                            apiSet.delete(api);
                        }
                    });
                }
            });
        }
        $cards.each(function() {
            var element = $(this);
            if (!apiSet || apiSet.has(element.attr('id').toLowerCase())) {
                element.removeClass('hide');
            } else {
                element.addClass('hide');
            }
        });
        if (apiSet && apiSet.size === 0) {
            $('#search').addClass('invalid');
            Materialize.toast('Could not find any results!', 4000, 'light-red');
        } else {
            $('#search').removeClass('invalid');
        }
    }

    $loadJSONPromise.done(function() {
        var parsedQuery = parseQuery(query);
        if (parsedQuery) {
            runQuery(parsedQuery);
        }
        $('#search').change(function(e) {
            var query = $('#search').val();
            runQuery(query);
        });
    });
});
