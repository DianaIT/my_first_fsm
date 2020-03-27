#! /usr/bin/env python
import rospy
from smach import State, StateMachine
from time import sleep
import actionlib
from jinko_service_msg.srv import jinko_service_msg, jinko_service_msgRequest, jinko_service_msgResponse

class A(State):
    def __init__(self):
        State.__init__(self, outcomes=['1', '0'], input_keys=['input'], output_keys=[''])

    def execute(self, userdata):
        sleep(1)
        if userdata.input == 1:
            return '1'
        else:
            return '0'


class B(State):
    def __init__(self):
        State.__init__(self, outcomes=['1', '0'], input_keys=['input'], output_keys=[''])

    def execute(self, userdata):
        sleep(1)
        if userdata.input == 1:
            return '1'
        else:
            return '0'

class C(State):
    def __init__(self):
        State.__init__(self, outcomes=['1', '0'], input_keys=['input'], output_keys=[''])

    def execute(self, userdata):
        sleep(1)
        if userdata.input == 1:
            return '1'
        else:
            return '0'

class D(State):
    def __init__(self):
        State.__init__(self, outcomes=['1', '0'], input_keys=['input'], output_keys=[''])

    def execute(self, userdata):
        sleep(1)
        if userdata.input == 1:
            return '1'
        else:
            return '0'

def turnOnStateMachine(request):

    sm = StateMachine(outcomes=['success'])
    sm.userdata.direction = request.direction
    with sm:
        StateMachine.add('A', A(), transitions={'1': 'B', '0': 'D'},
                             remapping={'input': 'direction', 'output': ''})
        StateMachine.add('B', B(), transitions={'1': 'C', '0': 'success'},
                             remapping={'input': 'direction', 'output': ''})
        StateMachine.add('C', C(), transitions={'1': 'D', '0': 'B'},
                             remapping={'input': 'direction', 'output': ''})
        StateMachine.add('D', D(), transitions={'1': 'success', '0': 'C'},
                             remapping={'input': 'direction', 'output': ''})

    ## sis = smach_os.IntrospectionServer('server_name', sm, '/SM_ROOT')
    ## sis.start()
    sm.execute()
    ## sis.stop()
    response = jinko_service_msgResponse()
    response.success = True
    return response

class main():
    def __init__(self):
        rospy.init_node('test_fsm', anonymous=True)
        rospy.Service('/jinko_navigation', jinko_service_msg, turnOnStateMachine)
        rospy.spin()

if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo(" Testeo practica ROSWeb & Maquina de estados finalizado")

