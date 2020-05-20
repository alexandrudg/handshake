import json
from operator import itemgetter
with open('citylots.json') as data_file:
  data = json.load(data_file)

def find_coordinates():
  file_emost_point = None
  file_wmost_point = None

  # some helper lambda functions
  get_long_extremity_point = lambda coords, extremity: extremity(coords, key = lambda x: x[0])

  for feature in data["features"]:

    feature_street = feature["properties"]["STREET"]

    if(feature_street == "ALEMANY"):
      feature_coordinates = feature["geometry"]["coordinates"][0]
      feature_emost_point = get_long_extremity_point(feature_coordinates, max)
      feature_wmost_point = get_long_extremity_point(feature_coordinates, min)

      if(file_emost_point is None):
        file_emost_point = feature_emost_point
      else:
        file_emost_point = get_long_extremity_point([feature_emost_point,file_emost_point], max)
        print(file_emost_point)

      if(file_wmost_point is None):
        file_wmost_point = feature_wmost_point
      else:
        file_wmost_point = get_long_extremity_point([feature_wmost_point,file_wmost_point], min)

  print '{0:.17f}'.format(file_wmost_point[0]), '{0:.17f}'.format(file_emost_point[0])

find_coordinates()
-122.470332640636968


      # def log_point(feature_point, file_point, cardinal):
      #   if(file_point is None):
      #     if(cardinal = "East"):
      #       file_point = feature_point
      #     elif(cardinal = "West"):
      #       file_point = feature_point
      #   else:
      #     file_emost_point = get_long_extremity_point([feature_emost_point,file_emost_point], min)
