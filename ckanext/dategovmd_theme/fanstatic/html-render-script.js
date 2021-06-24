function renderHTML() {
    var element, elements, html_string, xhttp;
    elements = document.getElementByTagName("*");
    for(let index = 0; index < elements.length; index++) {
        element = elements[index];
	html_string = element.getAttribute("raw_html");
	if(html_string) {
	
	}
    }
}
