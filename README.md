# xml2json

Server app based on microframework Flask

This app waits for POST request on 0.0.0.0:80 with xml data and
returns it in json format

Documentation is in appf.html

## Usage
- create image and then run:

  `./gradlew createImage`
  
  `docker run -p 80:80 myserver python3 appf.py`

  
- send POST request with xml payload to transform data to json on 0.0.0.0:80/xml with 6 different schemes



## Example

- Request: `curl -d "<hello>world</hello>" -X POST http://0.0.0.0:80/xml`
- Answer: `{"abdera":{"hello":"world"},"badgerfish":{"hello":{"$":"world"}},"cobra":{"hello":"world"},"gdata":{"hello":{"$t":"world"}},"parker":"world","yahoo":{"hello":"world"}}`
