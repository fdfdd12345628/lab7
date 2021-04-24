# SA/NA lab7

A simple key-value RESTful database.

## requirement
https://docs.google.com/presentation/d/1ZpDiDlmQcgis3OYAgolMfHTVMyiU5BfdUpTfULC9b8c/edit#slide=id.p

- POST /set/<KEY>
    - POST body: value=<VALUE>  (use application/x-www-form-urlencoded)
    - No other parameters
    - If successful, return string “OK”
    - If key exists, overwrite existing value with new value
- GET /get/<KEY>
    - No other parameters
    - Should return value for this key
    - If no key entry, return string “key not found!”
    
The maximum length of key/value is 256

