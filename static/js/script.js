
function year_check()
{
    var input = document.getElementById('year_purchase').value;
    // console.log(input)
    if (input.length !== 4 || isNaN(input)) {
        alert("Please enter a valid year in 'YYYY' format");
    }
}
function handler(event)
{
    event.preventDefault();
}

function get_data()
{
    document.querySelector('form').addEventListener('submit', handler);

    var fd = new FormData(document.querySelector('form'));

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/predict', true);

    xhr.onreadystatechange = function()
    {
        if(xhr.readyState == XMLHttpRequest.DONE)
        {
            document.getElementById('prediction').innerHTML = "Predicted Price: ₹"+ xhr.responseText;
            document.getElementById('prediction').style.display = 'block';
        }
    }

    xhr.onload = function(){};
    xhr.send(fd);
}