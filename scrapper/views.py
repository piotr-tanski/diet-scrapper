from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import get_diet
import json


def index(request):
    return HttpResponse('''
<!DOCTYPE html>
<html lang="en">
<head>
<title>Diet Scrapper</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<h1>Diet Scrapper</h1>
<pre id="maczfit">Loading...</pre>

<script>
function loadDiet(diet) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    console.log("XMLHttpRequest state changed:", this.readyState, this.status)
    if (this.readyState == XMLHttpRequest.DONE) {
      if (this.status === 0 || (this.status >= 200 && this.status < 400)) {
        document.getElementById(diet).innerHTML = JSON.stringify(JSON.parse(this.responseText), null, 2);
      } else if (this.status >= 400 && this.status < 500) {
        document.getElementById(diet).innerHTML = "Could not find!"
      } else if (this.status >= 500) {
        document.getElementById(diet).innerHTML = "Error occurred! Try again later."
      }
    }
  };
  xhttp.open("GET", "diet?diet=" + diet, true);
  xhttp.send();
}
loadDiet("maczfit")
</script>

</body>
</html>
''')


def diet(request):
    if request.method == "GET":
        diet = request.GET.get("diet")
        content = get_diet(diet)
        json_content = json.dumps(content)
        return HttpResponse(json_content, content_type='text/json')
    return HttpResponseBadRequest
