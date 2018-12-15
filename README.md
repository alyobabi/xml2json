# xml2json

Server app based on microframework Flask

This app waits for POST request on 0.0.0.0:80 with xml data and
returns it in json format

## Usage

- send POST request with xml payload to transform data to json on 0.0.0.0:80/xml with 6 diffrent schemes
- send POST request with xml payload to transform data to json on 0.0.0.0:80/xml_abdera with abdera scheme
- send POST request with xml payload to transform data to json on 0.0.0.0:80/xml_badgerfish with badgerfish scheme 
- send POST request with xml payload to transform data to json on 0.0.0.0:80/xml_cobra with cobr scheme
- send POST request with xml payload to transform data to json on 0.0.0.0:80/xml_gdata with gdata scheme
- send POST request with xml payload to transform data to json on 0.0.0.0:80/xml_parker with parker scheme
- send POST request with xml payload to transform data to json on 0.0.0.0:80/xml_yahoo with yahoo scheme

## Example

Request: curl -d "<hello>world</hello>" -X POST http://0.0.0.0:80/xml
Answer: {"abdera":{"hello":"world"},"badgerfish":{"hello":{"$":"world"}},"cobra":{"hello":"world"},"gdata":{"hello":{"$t":"world"}},"parker":"world","yahoo":{"hello":"world"}}
