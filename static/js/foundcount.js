$(document).ready(function() {
    $.ajax({
        url: '/foundcount',
        dataType: 'json',
        success: function(data) {
            $.each(data, function(category, count) {
                $('#categoryTableBody').append('<tr><td>' + category + '</td><td>' + count + '</td></tr>');
            });
        },
        error: function(xhr, status, error) {
            console.error('Error fetching data:', error);
        }
    });
});