# Racing line using Waypoints
def reward_function(params):
    left = [35, 36, 37, 100, 101, 102, 103, 111, 112, 113, 114, 115,
            121, 122, 123, 161, 162, 163, 164, 165, 166, 209, 210, 211, 212]

    centerleft = [1, 2, 3, 4, 5, 6, 7, 8, 9, 31, 63, 64, 65, 66, 93, 94, 132, 133, 134, 135, 147, 148, 149, 150, 151, 152, 153, 154,
                  155, 174, 206, 207, 208, 213, 214, 215, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259]

    centerright = [43, 60, 61, 62, 91, 92, 136, 137,
                   138, 145, 146, 192, 193, 204, 205, 216, 217]

    right = [22, 23, 24, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
             85, 86, 87, 139, 140, 141, 181, 182, 183, 184, 185, 200, 201, 202, 203, 218, 219, 220, 221, 222, 227, 228, 229, 230]

    fast = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 88, 89, 90, 91, 92, 93, 127, 128, 129, 130, 131, 132, 147, 148, 149, 150,
            151, 171, 172, 173, 174, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258]

    medium = [18, 19, 20, 21, 24, 25, 43, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 80, 81, 83, 84, 85, 86, 87, 94, 95, 96, 106, 107, 108, 109, 110, 111, 114, 115, 116, 117, 118, 122, 123, 124, 125, 126,
              133, 134, 135, 144, 145, 146, 152, 153, 154, 155, 169, 170, 175, 176, 177, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 199, 200, 201, 202, 217, 218, 219, 220, 221, 222, 223, 224, 225, 229, 230, 231, 232, 233, 234]

    slow = [22, 23, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 72, 73, 74, 75, 76, 77, 78, 79, 82, 97, 98, 99, 100, 101, 102, 103, 104, 105, 112, 113, 119, 120, 121, 136,
            137, 138, 139, 140, 141, 142, 143, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 198, 226, 227, 228]

    closest = params['closest_waypoints']
    nextwaypoint = max(closest[0], closest[1])

    if not params['all_wheels_on_track']:
        return 1.0e-3

    position_weight = 30.0
    ok_position_weight = 5.0

    speed_weight = 10.0
    ok_speed_weight = 2.0

    fast_threshold = 3
    medium_threshold = 2
    slow_threshold = 1

    reward = 5.0 # default reward for being on-track
    if (nextwaypoint in centerleft):
        if (params['distance_from_center']/params['track_width']) <= 0.25 and (params['is_left_of_center']):
            reward += position_weight
        elif (params['distance_from_center']/params['track_width']) <= 0.25 and (not params['is_left_of_center']):
            reward += ok_position_weight

    elif (nextwaypoint in centerright):
        if (params['distance_from_center']/params['track_width']) <= 0.25 and (not params['is_left_of_center']):
            reward += position_weight
        elif (params['distance_from_center']/params['track_width']) <= 0.25 and (params['is_left_of_center']):
            reward += ok_position_weight

    elif (nextwaypoint in left):
        if (params['is_left_of_center']) and (params['distance_from_center']/params['track_width']) > 0.25 and (params['distance_from_center']/params['track_width']) < 0.48:
            reward += position_weight
        elif (params['distance_from_center']/params['track_width']) <= 0.25 and (params['is_left_of_center']):
            reward += ok_position_weight

    elif (nextwaypoint in right):
        if (not params['is_left_of_center']) and (params['distance_from_center']/params['track_width']) > 0.25 and (params['distance_from_center']/params['track_width']) < 0.48:
            reward = position_weight
        elif (params['distance_from_center']/params['track_width']) <= 0.25 and (not params['is_left_of_center']):
            reward += ok_position_weight

    if nextwaypoint in fast:
        if params['speed'] >= fast_threshold:
            reward += speed_weight
        elif params['speed'] >= medium_threshold:
            reward += ok_speed_weight
    elif nextwaypoint in medium:
        if params['speed'] >= medium_threshold:
            reward += speed_weight
        elif params['speed'] >= slow_threshold:
            reward += ok_speed_weight
    elif nextwaypoint in slow:
        if params['speed'] <= slow_threshold:
            reward += speed_weight
        if params['speed'] <= medium_threshold:
            reward += ok_speed_weight

    return float(reward)

