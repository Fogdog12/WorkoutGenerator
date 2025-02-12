import random

# warm up lists
leg_day_warm_up = ['Side to Side Rotations', 'Rotating Toe Touches', 'Open Gate (L)', 'Open Gate (R)', 'Close gate (L)', 'Close Gate (R)',
                   'Hip Openers']

core_warm_up = ['Side to Side Rotations', 'Cross-body Shoulder Stretch (R)', 'Cross-body Shoulder Stretch (L)', 'Elbow Rotation (External)',
                'Elbow Rotations (Internal)', 'Side Bends', 'Rotating Toe Touches','Lunge with Rotation', 'Hip Openers']

back_and_chest_warm_up = ['Side Bends', 'Side to Side Rotations', 'Elbow Rotation (External)', 'Elbow Rotations (Internal)',
                            'Rotating Toe Touches', 'Hip Openers']

total_body_warm_up = ['Side Bends', 'Side to Side Rotations', 'Elbow Rotation (External)', 'Elbow Rotations (Internal)',
                            'Rotating Toe Touches', 'Open Gate (L)', 'Open Gate (R)', 'Close gate (L)', 'Close Gate (R)',
                      'Knee Rotation (Clockwise)', 'Knee Rotation (Counter Clockwise)', 'Hip Openers']

arms_warm_up = ['Cross-body Shoulder Stretch (R)', 'Cross-body Shoulder Stretch (L)', 'Elbow Rotation (External)',
                'Elbow Rotations (Internal)', 'Side to Side Rotations', 'Side Bends', 'Rotating Toe Touches']

# Leg Day Dictionary
legs = ['Front Lunges','Reverse Lunges','Single Leg Glute Bridges(R&L)','Prone Leg Raises','Single Prone Leg Raise (L&R)','Prisoner Squat',
       'Side Lunges (R&L)','Donkey Kicks (R&L)','Squat','Sumo Squat','Stance Jacks','Sqauts with Kickback',
        'Side Step Squats','Ice Skaters','Crossover Touch Squat','Lunge with Rotation','Squat with Calf Raise','Calf Raise',
       'Inward Calf Raise','Outward Calf Raise','Single Leg Squat (R&L)','Bird Dogs','Half Squat Walk','Wall Sit','Glute Bridges','Glute Bridges with Abduction',
       'Jump Lunges','Single Leg Calf Raise (R&L)']

# Core day Dictionary
core = ['Crunches','Elbow to Knee Crunch','Flutter Kicks','Single Leg V-Up (R&L)','Suitcase Crunches','Elbow Plank',
       'Side Knee Plank with Twist (R&L)','Seated Oblique Twist','Kayak Abs','Knee Claps','Dead Bug','Peekaboos','Side Knee Plank (R&L)',
       'Knee Plank with Alternating Arm Raises','Scissors','Spider Cross Plank','Airplane Plank','Table Leg Press','Partial Sit-Ups','Slow Mountain Climers',
       'Bicycle Crunches','Oblique Crunches (R&L)','Oblique Crunches with Opposite Elbow to Knee (R&L)','Standing Elbow to Knee','Heisman Move',
       'Standing Side Crunch (R&L)']

# Back and Chest Dictionary
back_chest = ['Downward Dog Toe Touch','Mountain CLimber to Push-Up from Knees','Lying Scorpion','Bird Dogs','Scarecrow',
             'Prone Leg Raises','Back Raise from the Floor','Side Knee Plank (R&L)','Single Leg Deadlifts (R&L)','Spiderman',
             'High Plank','Reverse Forearm Plank','Side Plank (R&L)','Plank to Downward Dog','Push-up Plank',
              'Single Prone Leg Raise (L&R)','Scarecrow','Superman Rows','Walkout to Push-ups','Mountain CLimber to Push-Up',' Divebomber Push-Ups',
              'Lying Leg Extensions to the (R&L)','Plank Jack Shoulder Taps','Push-Ups','Back Raise from the Floor','Walkouts to Forearm Plank',
              'Knee Plank with Alternating Arm Raises','Robot Arms']

# Total Body Dictionary
body = ['Step Up with Knee Raise','Sqauts with Kickback','Squat with Calf Raise','Single Leg Deadlift (R&L)','Calf Raise','Calf Raid Hold',
       'Knee Claps','Elbow to Knee Crunch','Reverse Sit-Ups','High Plank Walk Out','Ice Skaters with Shuffle Step','Mule Kicks','Butt Kicks',
       'Jumping Lunge','Reverse Lunge Kick (R&L)','Robot Arms','Reverse Forearm Plank','Sit Ups','Single Leg Toe Touch','Crunches','Partial Sit-Ups',
       'Crossover Touch Squat','Burpee Walk','Back Raise from the Floor','Side Step Plank','Side Knee Plank (R&L)','Side to Side Hop',
       'Slow Mountain Climbers','Jogging Jabs','Side to Side Floor Hops','Burpees','Plie Squat with Heel Raise','Switch Kicks',
       'Single Leg Push-Ups (R&L)','Low Impact Jumping Jacks','Chair Dips','Divebomber Push-ups','Prone Leg Raises','Single Prone Leg Raise (R&L)']

# Arms Dictionary
arms = ['Walkout to Push-ups','Single Leg Push-Ups (R&L)','Push-Ups','Narrow Push_ups from Knees','Side Knee Plank (R&L)','Elbow Plank',
       'Plank to Downward Dog','Mountain Climber to Push-Up from Knees','United Bicep','Push-Up plank','Prayer Pulse','Chair Dips',
       'Side Knee Plank with Elbow to Knee (R&L)','Robot Arms','Downward Dog Toe Touch','High Plank Walk Out','Mountain Climber to Push-Up',
       'Divebomber Push-Ups','Reverse Forearm Plank','Walkouts to Forearm Plank','Narrow Grip Push-Ups','Plank Arm and Leg Raise']

#cool Down
leg_day_cool_down = ['Standing Quad Stretch (R&L)','Lunge with Internal Rotation (R&L)', 'Figure 4 Stretch (L&R)','Cross-Legged Chest to Floor']

core_cool_down = ['Overhead Lat Stretch (R&L)','Lunge with Internal Rotation (R&L)','Side Stretch (R&L)','Mermaid (R&L)','Cobra']

back_and_chest_cool_down = ['Cross-Body Shoulder Stretch (R&L)','Overhead Lat Stretch (R&L)','Seated Lower Back Stretch (R&L)','Open Book (R&L)','Child Pose']

total_body_cool_down = ['Cross-Body Shoulder Stretch (R&L)','Lunge with Internal Rotation (R&L)','Overhead Lat Stretch (R&L)','Cobra','Seated Lower Back Stretch (R&L)','Figure 4 Stretch (L&R)','Cross-Legged Chest to Floor','Child Pose']

arms_cool_down = ['Overhead Lat Stretch (R&L)','Seated Lower Back Stretch (R&L)','Side Stretch (R&L)','Mermaid (R&L)','Open Book (R&L)','Child Pose']

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

print (style.BOLD + 'Back and Chest Day' + style.END)
print('_____________________________________\n')

print(style.BOLD + 'Warm Up' + style.END)
print(back_and_chest_warm_up)
print('_____________________________________\n')

circuits = random.randint(3, 5)
time_length = (20,30,45)

#function to create how many times will a cycle repeat
for x in range(circuits):
 
    #function to generate 3-5 exercises per circuit   
    wo = random.sample(back_chest,random.randint(2, 3))
    print(wo)
    print()
    #function for how many times to repeat circuit
    repeat = random.randint(1,3)
    print(f'Repeat circuit {repeat} times.\n')

    #function to generate how long (20,45,60s) and assign to exercises
    time = random.choice(time_length)
    print(f'Each exercise is {time} seconds long.\n')
    print(f'Take a 10 seconds to prepare for the next exercise.\n')
    print(f'60 second rest between circuits.')
    print('_____________________________________\n')
    
print(style.BOLD + 'Cool Down' + style.END)
print(back_and_chest_cool_down)
print('Do exercises for 30 seconds.')
print('_____________________________________\n')

print (style.BOLD + 'Core Day' + style.END)
print('_____________________________________\n')

print(style.BOLD + 'Warm Up' + style.END)
print(core_warm_up)
print('_____________________________________\n')

circuits = random.randint(3, 5)
time_length = (20,30,45)

#function to create how many times will a cycle repeat
for x in range(circuits):
 
    #function to generate 3-5 exercises per circuit   
    wo = random.sample(core,random.randint(2, 3))
    print(wo)
    print()
    #function for how many times to repeat circuit
    repeat = random.randint(1,3)
    print(f'Repeat circuit {repeat} times.\n')

    #function to generate how long (20,45,60s) and assign to exercises
    time = random.choice(time_length)
    print(f'Each exercise is {time} seconds long.\n')
    print(f'Take a 10 seconds to prepare for the next exercise.\n')
    print(f'60 second rest between circuits.')
    print('_____________________________________\n')
    
print(style.BOLD + 'Cool Down' + style.END)
print(core_cool_down)
print('Do exercises for 30 seconds.')
print('_____________________________________\n') 

print (style.BOLD + 'Leg Day' + style.END)
print('_____________________________________\n')

print(style.BOLD + 'Warm Up' + style.END)
print(leg_day_warm_up)
print('_____________________________________\n')

circuits = random.randint(3, 5)
time_length = (20,30,45)

#function to create how many times will a cycle repeat
for x in range(circuits):
 
    #function to generate 3-5 exercises per circuit   
    wo = random.sample(legs,random.randint(2, 3))
    print(wo)
    print()
    #function for how many times to repeat circuit
    repeat = random.randint(1,3)
    print(f'Repeat circuit {repeat} times.\n')

    #function to generate how long (20,45,60s) and assign to exercises
    time = random.choice(time_length)
    print(f'Each exercise is {time} seconds long.\n')
    print(f'Take a 10 seconds to prepare for the next exercise.\n')
    print(f'60 second rest between circuits.')
    print('_____________________________________\n')
    
print(style.BOLD + 'Cool Down' + style.END)
print(leg_day_cool_down)
print('Do exercises for 30 seconds.')
print('_____________________________________\n') 

print (style.BOLD + 'Arms Day' + style.END)
print('_____________________________________\n')

print(style.BOLD + 'Warm Up' + style.END)
print(arms_warm_up)
print('_____________________________________\n')

circuits = random.randint(3, 5)
time_length = (20,30,45)

#function to create how many times will a cycle repeat
for x in range(circuits):
 
    #function to generate 3-5 exercises per circuit   
    wo = random.sample(arms,random.randint(2, 3))
    print(wo)
    print()
    #function for how many times to repeat circuit
    repeat = random.randint(1,3)
    print(f'Repeat circuit {repeat} times.\n')

    #function to generate how long (20,45,60s) and assign to exercises
    time = random.choice(time_length)
    print(f'Each exercise is {time} seconds long.\n')
    print(f'Take a 10 seconds to prepare for the next exercise.\n')
    print(f'60 second rest between circuits.')
    print('_____________________________________\n')
    
print(style.BOLD + 'Cool Down' + style.END)
print(arms_cool_down)
print('Do exercises for 30 seconds.')
print('_____________________________________\n')   

print (style.BOLD + 'Total Body Day' + style.END)
print('_____________________________________\n')

print(style.BOLD + 'Warm Up' + style.END)
print(total_body_warm_up)
print('_____________________________________\n')

circuits = random.randint(3, 5)
time_length = (20,30,45)

#function to create how many times will a cycle repeat
for x in range(circuits):
 
    #function to generate 3-5 exercises per circuit   
    wo = random.sample(body,random.randint(2, 3))
    print(wo)
    print()
    #function for how many times to repeat circuit
    repeat = random.randint(1,3)
    print(f'Repeat circuit {repeat} times.\n')

    #function to generate how long (20,45,60s) and assign to exercises
    time = random.choice(time_length)
    print(f'Each exercise is {time} seconds long.\n')
    print(f'Take a 10 seconds to prepare for the next exercise.\n')
    print(f'60 second rest between circuits.')
    print('_____________________________________\n')
    
print(style.BOLD + 'Cool Down' + style.END)
print(total_body_cool_down)
print('Do exercises for 30 seconds.')
print('_____________________________________\n')
