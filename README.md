# rdm-metadata-webform-dev

In the `xsdforms` directory, there are xsd (XML Schema Definition) files that can be fed into [the service](https://xsd-forms.herokuapp.com) to generate web-forms and the javascripts for exporting form data in XML format.

The conversion is done via this [software package](https://github.com/davidmoten/xsd-forms). 

The converted forms are accessible via the following links:

 - [DAC](http://rdmapptst.uci.ru.nl/rdm-mdforms/dac)
 - [SIC](http://rdmapptst.uci.ru.nl/rdm-mdforms/sic)
 
Upon the submission, the form data are __POST__-ed via __XMLHttpRequest__ to the cgi-bin scripts running on the same web server.  The source codes of the cgi-bin scripts are available in the `cgi-bin` directory in this repository.
