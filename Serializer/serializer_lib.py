#! /usr/bin/env python

# from any_pb2 import Any
# from fleet_planning_pb2 import FleetPlanning
# from distributed_estimation_pb2 import DistributedEstimation
import any_pb2
import fleet_planning_pb2

class Serializer(object):

    def __init__(self):
        self.types = {
            # "dist_est":     (self.distributed_estimation_pb2, ROS_topic),
            "fleet_plan":   (fleet_planning_pb2, "ROS_topic")
        }

    # Serializes messages in two step using name (dist_est / fleet_plan) 
    def Serialize(self, name, ROS_msg):

        # Extract ROS_topic from types dictionary
        self.ROS_topic = self.types[name][1]

        self.ROS_msg = ROS_msg

        if name == "dist_est":
            # Serialize data (distributed_estimation.proto)
            self.dist_est = self.types[name][0].DistributedEstimation()

            self.data = self.dist_est.SerializeToString()
            

        elif name == "fleet_plan":
            # Serialize data (fleet_planning.proto)
            self.fleet_plan = self.types[name][0].FleetPlanning()

            self.fleet_plan.robot_name = self.ROS_msg.robot_name
            # self.fleet_plan.transform = self.ROS_msg.transform
            self.fleet_plan.transform.translation.x = self.ROS_msg.transform.translation.x
            self.fleet_plan.transform.translation.y = self.ROS_msg.transform.translation.y
            self.fleet_plan.transform.translation.z = self.ROS_msg.transform.translation.z
            self.fleet_plan.transform.rotation.x = self.ROS_msg.transform.rotation.x
            self.fleet_plan.transform.rotation.y = self.ROS_msg.transform.rotation.y
            self.fleet_plan.transform.rotation.z = self.ROS_msg.transform.rotation.z
            self.fleet_plan.transform.rotation.w = self.ROS_msg.transform.rotation.w
            self.fleet_plan.status_info = self.ROS_msg.status_info

            self.data = self.fleet_plan.SerializeToString()
            

        # Pack the message (any.proto)

        self.any_msg = any_pb2.Any()
        self.any_msg.type_url = name
        self.any_msg.value = self.data
        self.any_data = self.any_msg.SerializeToString()

    # Serializes messages in two step using name (dist_est / fleet_plan) 
    def Deserialize(self, Proto_msg):
        # Unpack the Any() message
        self.any_msg = any_pb2.Any()
        self.any_msg.ParseFromString(Proto_msg)

        # Unpack the message
        if self.any_msg.type_url == "dist_est":
            self.dist_est = self.types[name][0].DistributedEstimation()
            self.dist_est = self.dist_est.ParseFromString(any_msg)

        elif self.any_msg.type_url == "fleet_plan":
            self.fleet_plan = self.types[name][0].FleetPlanning()
            self.fleet_plan.ParseFromString(any_msg.value)


        









    # def Deserialize(self, ):

### TESTING ###

if __name__ == "__main__":
    serial = Serializer()
    print serial.types["fleet_plan"][1]
    # print serial.Serialize.any_data

    # Creat dummy data for fleet planning

    fleet_plan = fleet_planning_pb2.FleetPlanning()

    fleet_plan.robot_name = "anybot"
    
    fleet_plan.transform.translation.x = 1
    fleet_plan.transform.translation.y = 1
    fleet_plan.transform.translation.z = 1

    fleet_plan.transform.rotation.x = 2
    fleet_plan.transform.rotation.y = 2
    fleet_plan.transform.rotation.z = 2
    fleet_plan.transform.rotation.w = 2

    fleet_plan.status_info = 4

    serial.Serialize("fleet_plan", fleet_plan)

    print serial.any_data





### TESTING ###