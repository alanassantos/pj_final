import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped

class Pose(Node):
    def __init__(self):
        super().__init__('Pose')

        self.gzpr_publisher_tf_carrinho = self.create_publisher(TFMessage, '/tf_carrinho', 10)
        self.gzpr_publisher_tf_static = self.create_publisher(TFMessage, '/tf_static', 10)

        self.subscriptioncarrinho = self.create_subscription(
            TransformStamped,
            '/model/carrinho/pose',
            self.p_callback,
            10)
        
        self.subscriptionstatic = self.create_subscription(
            TransformStamped,
            '/model/carrinho/pose_static',
            self.s_callback,
            10
        )

    def p_callback(self, msg):
        TF_Message = TFMessage()
        TF_Message.transforms.append(msg)
        self.gzpr_publisher_tf_carrinho(TF_Message)

    def s_callback(self, msg):
        TF_Message = TFMessage()
        TF_Message.transforms.append(msg)
        self.gzpr_publisher_tf_static(TF_Message)

def main(args=None):
    rclpy.init(args=args)
    mapear = Pose()

    try:
        rclpy.spin(mapear)
    except KeyboardInterrupt:
        pass

    mapear.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()