distance_mi=7
is_raining=True
has_bike=False
has_car=True
has_ride_share_app= True
Commute_Possible = False
if distance_mi == 0 or distance_mi==0.0 or distance_mi == False or distance_mi=='':
    Commute_Possible=False 
elif distance_mi <=1 and  is_raining ==False:
    Commute_Possible=True    
elif distance_mi <=1 and  is_raining ==True:
    Commute_Possible=False 
elif (distance_mi >1 and distance_mi <=6) and has_bike and is_raining==False: 
    Commute_Possible=True
elif distance_mi > 6 and has_car:
    Commute_Possible=True 
elif distance_mi > 6 and has_ride_share_app:
    Commute_Possible=True 
elif distance_mi>6 and (not has_car or not has_ride_share_app):
    Commute_Possible=False 
print(Commute_Possible)