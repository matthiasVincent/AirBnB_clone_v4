# Web dynamic
This is the fourth iteration of our AirBnB_clone projects. In this particular project, I learnt how to dynamically manipulate and modify DOM elements using JQuery library. I also learnt how to make API call to web resources and use the response to update the content of a given DOM element without page refresh

# Tasks
* ** 0. Last clone! **
forked my previous repository [AirBnB_clone_v3](https://github.com/matthiasVincent/AirBnB_clone_v3) and renamed it to `AirBnB_clone_v4`

* ** [1. Cash only](./0-hbnb.py) **
Script that start Flask web application and renders this [template](./templates/0-hbnb.html) when queried from the uri `/0-hbnb/`. A `uuid.uuid4()` varaiable `cache_id` was appended as a query string on each static assets path to prevent Flask application from catching the assets

* ** [2. Select some Amenities to be comfortable](./1-hbnb.py) **
Carry out the following to make the filter section in this [template](./templates/1-hbnb.html) dynamic:
    * Added an `input` tag of type `checkbox` to `li` tag of each amenity
    * Added property `data-id=":amenity_id"` and `data-name=":amenity_name` to the `input` tag of each `li` tags to be able to retrieve them from the DOM
    * This [script](./static/scripts/1-hbnb.js) was written to do the necessary DOM manipulation and update

* ** [3. API status](./2-hbnb.py) **
Updated the API entry point in this [file](../api/v1/app.py) by replacing the original CORS instance with `CORS(app, resources={r"/api/v1/*": {"origins": "*"}})` to enable cross origin resource sharing, added a new `div` tag with id attribute `api_status` in the `header` tag to show the status of my API. The dynamism therein is achieved using this [script](./static/scripts/2-hbnb.js)

* ** [4. Fetch places](./3-hbnb.py) **
Used JQuery `Ajax` to fetch places from the frontend through the API endpoint `http://0.0.0.0:5001/api/v1/places_search/`. To be able to get all the places on page load, an empty JSON was passed using `POST` request. Find the script [here](./static/scripts/3-hbnb.js)

* ** [5. Filter places by Amenity](./4-hbnb.py) **
Filters places by amenity when a `POST` request is made to the API endpoint `http://0.0.0.0:5001/api/v1/places_search/` through a `button` click after some amenities is checked. All done using JQuery and this [script](./static/scripts/4-hbnb.js)

* ** [6. States and Cities](./100-hbnb.py) **
Filters places by amenities, states and cities when a `POST` request is made to the API endpoint `http://0.0.0.0:5001/api/v1/places_search/` through a `button` click after some amenities, states or cities are checked. All done using JQuery and this [script](./static/scripts/100-hbnb.js)

# Author
[Matthias Sunday Oduh](https://github.com/matthiasVincent)
Portfolio site [here](https://matthias28908ue14.pythonanywhere.com)

