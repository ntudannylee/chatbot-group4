import googlemaps

# Client initialization
API_key = 'AIzaSyAPtgFF8msgOfa_CK_FevErxHxH6HGZ8EM'
gmaps = googlemaps.Client(key=API_key)

def googlemaps_search_location(place):
# 尋找位置的經緯度
# http形式： https://maps.googleapis.com/maps/api/geocode/json?address=%E5%8C%97%E8%BB%8A&key=AIzaSyAPtgFF8msgOfa_CK_FevErxHxH6HGZ8EM
    geocode_result = gmaps.geocode(place)
    x = geocode_result[0]['geometry']['location']['lat']
    y = geocode_result[0]['geometry']['location']['lng']
    return (x,y)

def googlemaps_search_nearby(x,y,place_type):
    location = (x, y)
    print(location)
    radius = 1000    #1km
    place_type = 'restaurant'
    result = gmaps.places_nearby(location, radius, type=place_type)

    restaurants = result['results']
    restaurants_list=[]
    # sort the restaurant by its rating
    for i in restaurants:
        # 先過濾掉沒有rating的商店, 且使用者rating至少有300則
        if('rating' in i and i['user_ratings_total'] > 300):
            place_id=''
            rating= i['rating']
            business_status=''
            location_x=''
            location_y=''
            name=''
            photo_reference=''
            user_ratings_total=''
            address=''
            if('place_id' in i):
                place_id = i['place_id']
            if('business_status' in i):
                business_status = i['business_status']
            if('geometry' in i):
                location_x = i['geometry']['location']['lat']
                location_y = i['geometry']['location']['lng']
            if('name' in i):
                name = i['name']
            if('photos' in i):
                photo_reference = i['photos'][0]['photo_reference']
            if('user_ratings_total' in i):
                user_ratings_total = i['user_ratings_total']
            if('vicinity' in i):
                address = i['vicinity']
            # create each restaurant dict
            i = {            
                'place_id':place_id,
                'rating' : rating,
                'business_status':business_status,
                'location_x':location_x,
                'location_y':location_y,
                'name':name,
                'photo_reference':photo_reference,
                'user_ratings_total':user_ratings_total,
                'address':address
            }
            restaurants_list.append(i)

    # 以rating排序restaurant_list
    restaurants_list = sorted(restaurants_list, key=lambda k: k['rating'], reverse=True)
    # print(restaurants_list)
    # print('餐廳總數：', len(restaurants_list))
    return restaurants_list
    # output: [{'place_id': 'ChIJ_7BM_EupQjQRxeNc_Fq318U', 'rating': 4.7, 'business_status': 'OPERATIONAL', 'location_x': 25.015927, 'location_y': 121.508267, 'name': 'Sanyi Breakfast Restaurant', 'photo_reference': 'ATtYBwLW9QK5PLE3NMjt5h3WaLa8C_yEOzK5kdR1s7IQ-r01Z8m_IWfpfE_TJJBtWk8cqKz38uXMFBpef81omW_puXAfDZBij9Cm54UecYLsMKE10AfZwBxwsXH4r71xceZ1N_RM9iFqIx7v6Ias3EWIhufwjfvbBM9yaAXmkZ6GnNyvSgm9', 'user_ratings_total': 27, 'address': 'No. 32-1號, Xinsheng Road, Yonghe District'}, {'place_id': 'ChIJJehTKMGpQjQR7O6dPNfUD7M', 'rating': 4.6, 'business_status': 'OPERATIONAL', 'location_x': 25.0153732, 'location_y': 121.5090055, 'name': '古雲林鄉土小吃', 'photo_reference': 'ATtYBwIRq3McPQ8HgUjPOgTh4tz_h_aBErBGoPY1duwm1q5ndQet-_yRFhc5eIehy4GEppRycuvmstQ0GxdZtPxYgtC-1wqQH4Hpomga0oTFpPUbkLl7wGWBwK0MGOgEatmjVL64Vsfn6nbOfwIPmJb0LJ8RmkqxQxivNrOuoNB8udyYHrRW', 'user_ratings_total': 5, 'address': "1樓, No. 128號, Bao'an Road, Yonghe District"}, {'place_id': 'ChIJOWd4zsapQjQRNlfniqy08Co', 'rating': 4.4, 'business_status': 'OPERATIONAL', 'location_x': 25.014932, 'location_y': 121.508089, 'name': '陳記手工大陳年糕', 'photo_reference': '', 'user_ratings_total': 7, 'address': 'No. 5號, Alley 4, Lane 95, Xinsheng Road, Yonghe District'}, {'place_id': 'ChIJz997L4upQjQR5QyGw9BzIM4', 'rating': 4.3, 'business_status': 'OPERATIONAL', 'location_x': 25.0152105, 'location_y': 121.5089323, 'name': '外星人早午餐', 'photo_reference': 'ATtYBwJAgvl3Mvf5QnJq3t6rUyZeMnz8kpdaULkZeHojdLZck_GJgOitFzfBNV5IOR338tz6SaY4rAEkRDbstO7OtzZeh5cxVyYTzVTTHe1p-H5E9h9ngZ2baAXi1wJS5xShsq9UWWVMH8wQhziS-AeDhWB68hDoKJovowBrz0j9mwH21Qh4', 'user_ratings_total': 40, 'address': "No. 71-67, Bao'an Road, Yonghe District"}, {'place_id': 'ChIJBWNRNZmpQjQRmmDYtEXIpss', 'rating': 4, 'business_status': 'OPERATIONAL', 'location_x': 25.0143849, 'location_y': 121.507999, 'name': '保安路壹捌捌', 'photo_reference': 'ATtYBwKvYK-AFh988zajsk7uChNKGqrmz75cH7yDNy1GduxEY8ATEdB_eefsAQpMhJq6D945z1-ElpfcxRUsZ04dBJ2vd5n3YMt-KiqP9M-DGmm1eNbkHugl_0mdM1deE2QxQDj1WCCJPBLPvNSMBevzFH0m6caDd40oHkItMN342efUV424', 'user_ratings_total': 11, 'address': "No. 188號, Bao'an Road, Yonghe District"}, {'place_id': 'ChIJD9Q9KMGpQjQR5ykEJeHPcw4', 'rating': 3.9, 'business_status': 'OPERATIONAL', 'location_x': 25.015628, 'location_y': 121.509063, 'name': 'Dumpling Restaurant', 'photo_reference': 'ATtYBwIjqILQYOzFX-URvRBgMgriekAjhmu6FEINej_VIj702s14vi1mgdnhbrkNt8MqdBoFcSLPOPdHRqOOC-AUwRtBTWv0mxMLeRfDIUZZeXZTz271ejhOFiwxAaMHr1uB1_KG6tiU8JN3uHSq1AyydfQVDGnucF-VKKJtpd7ZdOhyHa3b', 'user_ratings_total': 41, 'address': "No. 124, Bao'an Road, Yonghe District"}, {'place_id': 'ChIJ7zxgwkapQjQRtgwZJ2OCJ_c', 'rating': 3.4, 'business_status': 'OPERATIONAL', 'location_x': 25.015376, 'location_y': 121.508845, 'name': '尚浩 魯肉飯 焢肉飯', 'photo_reference': 'ATtYBwKvoum1FMsOYCcze53Hs6VOvLNmp_zxXvO6fyKrn23-BMw3Ada6SjJ5P2AAqrI0LxLzp3QYpilGuD7QW0PsJqv49DLVTwDdaKuN_Hwo_63EmxO_g6esVuabsX6JP8OcP8OBlNfwnWXb0ufwsAHRhYcOSgTykNIRMoqGoLPsWCRXCMHS', 'user_ratings_total': 43, 'address': "No. 132號, Bao'an Road, Yonghe District"}]

# 供外界call的function
def googlemaps_API(place):
    x, y = googlemaps_search_location(place)
    restaurants = googlemaps_search_nearby(x,y,'restaurant')
    restaurants_name=[]
    # 只先取前五個
    for i in restaurants[0:5]:
        restaurants_name.append(i['name'])
    print(restaurants_name)

googlemaps_API('公館')