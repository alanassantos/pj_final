import rclpy 
from rclpy.node import Node
from rosgraph_msgs.msg import Clock 

class ClockT(Node):
    def __init__(self):
        super().__init__('Clock')
        self.publisher = self.create_publisher(Clock, '/clock', 10)
        self.subscription = self.create_subscription(
            Clock, 
            '/clock',
            self.clock_callback,
            10
        )
        self.timer = self.create_timer(1.0, self.publish_time)
        self.Timer = 0

    def publish_time(self):
        self.Timer += 1
        clockMSG = Clock()
        clockMSG.clock.sec = self.Timer
        self.publisher.publish(clockMSG)

    def clock_callback(self, msg):
        receberT = msg.clock.sec
        self.get_logger().info(f' Tempo do tópico /clock recebido: {receberT}s')

def main(args=None):
    rclpy.init(args=args)
    timesn = ClockT()
    try:
        rclpy.spin(timesn)
    except KeyboardInterrupt:
            pass
    
    timesn.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()