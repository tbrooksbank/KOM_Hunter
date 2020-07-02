from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException

# Configure OAuth2 access token for authorization: strava_oauth
from Main import access_token
swagger_client.configuration.access_token = access_token

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()


class strava_segments:

    def locate_segments(self):
        bounds =  # array[Float] | The latitude and longitude for two points describing a rectangular boundary for the search: [southwest corner latitutde, southwest corner longitude, northeast corner latitude, northeast corner longitude]
        try:
            # Explore segments
            api_response = api_instance.exploreSegments(bounds, activityType=running, minCat=minCat, maxCat=maxCat)
        except ApiException as e:
            print("Exception when calling SegmentsApi->exploreSegments: %s\n" % e)