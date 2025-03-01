/**
 * For form field country ( Django country ) Placeholder's colour
 * make the colour similar to other fields  
 */
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#737862');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#cdd6af;');
    } else {
        $(this).css('color', '#0e170f');
    }
});