let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', 'rgba(205, 214, 175, 0.7');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', 'rgba(205, 214, 175, 0.7');
    } else {
        $(this).css('color', '#0e170f');
    }
});