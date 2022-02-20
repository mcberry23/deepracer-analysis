from reward import *

params = {}
params["all_wheels_on_track"] = True
params["is_left_of_center"] = True
params["speed"] = 3.0
params["track_width"] = 0.5
params["distance_from_center"] = 0.1
params["closest_waypoints"] = [2, 3]

reward = reward_function(params)
print(reward)
