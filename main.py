#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_group_1_motor_a = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
motor_group_1_motor_b = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
motor_group_1 = MotorGroup(motor_group_1_motor_a, motor_group_1_motor_b)
motor_group_2_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_group_2_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
motor_group_2 = MotorGroup(motor_group_2_motor_a, motor_group_2_motor_b)
motor_6 = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
# vex-vision-config:begin
vision_12__R_SIG = Signature(1, 7337, 10181, 8759,-2115, -223, -1169,4, 0)
vision_12__G_SIG = Signature(2, -8119, -5825, -6972,-5509, -3317, -4413,3, 0)
vision_12__B_SIG = Signature(3, -3933, -3019, -3476,4159, 7333, 5746,2.5, 0)
vision_12__Y_SIG = Signature(4, -929, -413, -671,-4287, -3393, -3840,3.1, 0)
vision_12 = Vision(Ports.PORT12, 50, vision_12__R_SIG, vision_12__G_SIG, vision_12__B_SIG, vision_12__Y_SIG)
# vex-vision-config:end


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
vexcode_vision_12_objects = []
vexcode_vision_12_object_index = 0

# I have renamed all the events to more suitable names to make the code easier to read.
# I have also reformatted all the code to be in a sequential order based off when events happen in real life. (I haven't yet tested it so I dont know if it works. 30-05-2024)
# Later on 30-05-2024 - It definitely does NOT work     :skull:     More thinking required


    # I still don't have callibration for the Vision Sensor on my computer D:
    # Motors 20 & 11 are motor_group_1 (Right is 20, left is 11)  (The wheel motors)
    # Motors 1 & 10 are motor_group_2 (The arm motors)
    # Motor 6 is standalone (The claw motor)
    # Things to do:

    # Transfer motors to motor_groups          DONE!
    # Rewrite code for colour detection         DONE!
    # Change timings of - wait(-.-, SECONDS) - to be accurate
    # Zeb will write movement code  (IN PROGRESS!!!)
    # We must callibrate the signatures TODAY        DONE!

    # START 2 SHOULD NOT BRING IT BACK TO ITS ORIGINAL POSITION!!! (Same goes for everything else)




def when_started1():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    start()
motor_group_2.spin(REVERSE)
wait(1, SECONDS)
motor_group_2.stop()
    
def start():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_2.spin(REVERSE)
    wait(0.5, SECONDS)
    motor_group_2.stop()
    wait(0.1, SECONDS)
    motor_group_2.stop()
    vision_12.take_snapshot(vision_12__R_SIG)
    if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
            if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                claw()
            else:
                motor_group_2.spin(REVERSE)
                wait(0.5, SECONDS)
                motor_group_2.stop()
                vision_12.take_snapshot(vision_12__G_SIG)
                if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                    if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                        claw()
                    else:
                        motor_group_2.spin(REVERSE)
                        wait(0.5, SECONDS)
                        motor_group_2.stop()
                        vision_12.take_snapshot(vision_12__B_SIG)
                        if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                            if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                                claw()
                            else:
                                motor_group_2.spin(REVERSE)
                                wait(0.5, SECONDS)
                                motor_group_2.stop()
                                vision_12.take_snapshot(vision_12__Y_SIG)
                                if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                                    if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                                        claw()
                                    else:
                                        movement1() #Zeb will write this

def movement1():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1_motor_b.spin(FORWARD)
    wait(0.5, SECONDS)
    motor_group_1_motor_b.stop
    motor_group_1.spin(FORWARD)
    wait(0.5, SECONDS)
    motor_group_1.stop
    start()

                      # Claw code (for movement of the claw)

def claw(): #After this code, Zeb will need to write code to get the robot to the basket.
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    wait(0.5, SECONDS)
    motor_6.spin(FORWARD)
    wait(1, SECONDS)
    motor_6.stop() 
    #motor_group_2.spin(REVERSE)
    #wait(2, SECONDS)
    #motor_group_2.stop
    #motor_group_1.spin_for(FORWARD, 90, DEGREES)
    #start2.broadcast()
    basket1()

def basket1(): #This code will be movement from picking up the fuse to the basket
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_1_motor_a.spin(FORWARD)
    wait(2, SECONDS)
    motor_group_1_motor_a.stop
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_2.spin(REVERSE)
    wait(1, SECONDS)
    motor_group_2.stop
    motor_6.spin(REVERSE)
    wait(0.7, SECONDS)
    motor_6.stop
    start()


def start2():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1.spin(REVERSE)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_1_motor_b.spin(FORWARD)
    wait(2, SECONDS)
    motor_group_1_motor_b.stop
    motor_group_1.spin(REVERSE)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_2.spin(FORWARD)
    wait(1, SECONDS)
    motor_group_2.stop
    scan()
    

def scan():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    while True:
        vision_12.take_snapshot(vision_12__R_SIG)
        if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
            if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                claw2()
            else:
                vision_12.take_snapshot(vision_12__G_SIG)
                if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                    if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                        claw2()
                    else:
                        vision_12.take_snapshot(vision_12__B_SIG)
                        if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                            if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                                claw2()
                            else:
                                vision_12.take_snapshot(vision_12__Y_SIG)
                                if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                                    if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                                        claw2()
                                    else:
                                        movement2()

def movement2():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1_motor_b.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1_motor_b.stop
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop
    scan()

def claw2(): #After this code, Zeb will need to write code to get the robot to the basket.
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_6.spin(FORWARD)
    wait(1, SECONDS)
    motor_6.stop() 
    #motor_group_2.spin(REVERSE)
    #wait(2, SECONDS)
    #motor_group_2.stop
    #motor_group_1.spin_for(FORWARD, 90, DEGREES)
    #start2.broadcast()
    basket2()

def basket2(): #This code will be movement from picking up the fuse to the basket
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_1_motor_a.spin(FORWARD)
    wait(2, SECONDS)
    motor_group_1_motor_a.stop
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_2.spin(REVERSE)
    wait(1, SECONDS)
    motor_group_2.stop
    motor_6.spin(REVERSE)
    wait(0.7, SECONDS)
    motor_6.stop
    start3()

def start3():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1.spin(REVERSE)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_1_motor_b.spin(FORWARD)
    wait(2, SECONDS)
    motor_group_1_motor_b.stop
    motor_group_1.spin(REVERSE)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_2.spin(FORWARD)
    wait(1, SECONDS)
    motor_group_2.stop
    scan2()
    

def scan2():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    while True:
        vision_12.take_snapshot(vision_12__R_SIG)
        if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
            if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                claw3()
            else:
                vision_12.take_snapshot(vision_12__G_SIG)
                if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                    if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                        claw3()
                    else:
                        vision_12.take_snapshot(vision_12__B_SIG)
                        if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                            if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                                claw3()
                            else:
                                vision_12.take_snapshot(vision_12__Y_SIG)
                                if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                                    if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                                        claw3()
                                    else:
                                        movement3()

def movement3():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1_motor_b.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1_motor_b.stop
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop
    scan2()

def claw3(): #After this code, Zeb will need to write code to get the robot to the basket.
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_6.spin(FORWARD)
    wait(1, SECONDS)
    motor_6.stop() 
    #motor_group_2.spin(REVERSE)
    #wait(2, SECONDS)
    #motor_group_2.stop
    #motor_group_1.spin_for(FORWARD, 90, DEGREES)
    #start2.broadcast()
    basket3()

def basket3(): #This code will be movement from picking up the fuse to the basket
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3, movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_1_motor_a.spin(FORWARD)
    wait(2, SECONDS)
    motor_group_1_motor_a.stop
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_2.spin(REVERSE)
    wait(1, SECONDS)
    motor_group_2.stop
    motor_6.spin(REVERSE)
    wait(0.7, SECONDS)
    motor_6.stop
    start4()

def start4():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1.spin(REVERSE)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_1_motor_b.spin(FORWARD)
    wait(2, SECONDS)
    motor_group_1_motor_b.stop
    motor_group_1.spin(REVERSE)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_2.spin(FORWARD)
    wait(1, SECONDS)
    motor_group_2.stop
    scan3()
    

def scan3():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    while True:
        vision_12.take_snapshot(vision_12__R_SIG)
        if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
            if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                claw4()
            else:
                vision_12.take_snapshot(vision_12__G_SIG)
                if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                    if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                        claw4()
                    else:
                        vision_12.take_snapshot(vision_12__B_SIG)
                        if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                            if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                                claw4()
                            else:
                                vision_12.take_snapshot(vision_12__Y_SIG)
                                if vexcode_vision_12_objects and len(vexcode_vision_12_objects) > 0:
                                    if vexcode_vision_12_objects[vexcode_vision_12_object_index].width > 50 and vexcode_vision_12_objects[vexcode_vision_12_object_index].width < 350:
                                        claw4()
                                    else:
                                        movement4()

def movement4():
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1_motor_b.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1_motor_b.stop
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop
    scan3()

def claw4(): #After this code, Zeb will need to write code to get the robot to the basket.
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_6.spin(FORWARD)
    wait(1, SECONDS)
    motor_6.stop() 
    #motor_group_2.spin(REVERSE)
    #wait(2, SECONDS)
    #motor_group_2.stop
    #motor_group_1.spin_for(FORWARD, 90, DEGREES)
    #start2.broadcast()
    basket4()

def basket4(): #This code will be movement from picking up the fuse to the basket
    global myVariable, movement1, claw, claw2, claw3, claw4, start, start2, start3, start4, scan, scan2, scan3,  movement2, movement3, movement4, basket1, basket2, basket3, basket4, vexcode_vision_12_objects, vexcode_vision_12_object_index
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_1_motor_a.spin(FORWARD)
    wait(2, SECONDS)
    motor_group_1_motor_a.stop
    motor_group_1.spin(FORWARD)
    wait(1.5, SECONDS)
    motor_group_1.stop()
    motor_group_2.spin(REVERSE)
    wait(1, SECONDS)
    motor_group_2.stop
    motor_6.spin(REVERSE)
    wait(0.7, SECONDS)
    motor_6.stop
    # May broadcast something to end the code if I have time


    wait(5, MSEC)
        
# system event handlers
claw()
claw2()
claw3()
claw4()
start()
movement1()
movement2()
movement3()
movement4()
basket1()
basket2()
basket3()
basket4()
scan()
scan2()
scan3()

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()





        
        

    
