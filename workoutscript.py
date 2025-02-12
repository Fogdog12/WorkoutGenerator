import random
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
