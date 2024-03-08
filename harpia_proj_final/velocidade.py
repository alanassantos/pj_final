# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist

# class VelocidadePublisher(Node):

#     def __init__(self):
#         super().__init__('VelocidadePublisher')
#         self.publisher = self.create_publisher(Twist, 'diff_drive/cmd_vel', 10)
#         self.timerr = 1.0
#         self.timer = self.create_timer(self.timerr, self.publica)

#     def publica(self):
#         self.Velmsg = Twist()
#         self.Velmsg.linear.x = 5.0
#         self.Velmsg.angular.z = 0.5

#         self.publisher.publish(self.Velmsg)
#         self.get_logger().info(f'Publicando velocidade linear de: {self.Velmsg.linear.x} e angular de: {self.Velmsg.angular.z}')

# def main(args=None):
#     rclpy.init(args=args)
#     velocidadeCarrinho = VelocidadePublisher()
#     try:
#         rclpy.spin(velocidadeCarrinho)
#     except KeyboardInterrupt:
#         pass
        
#     velocidadeCarrinho.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelocidadeControlador(Node):
    def __init__(self):
        super().__init__('velocidade_controlador')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(1, self.publicar_velocidade)
        self.velocidade = Twist()

    def publicar_velocidade(self):
        self.publisher.publish(self.velocidade)
        self.get_logger().info(f'Publicando comando de velocidade: Linear - {self.velocidade.linear.x}, Angular - {self.velocidade.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    controlador = VelocidadeControlador()
    
    # Defina as velocidades linear e angular conforme necessário
    controlador.velocidade.linear.x = 0.5  # Velocidade linear de 0.5 m/s
    controlador.velocidade.angular.z = 0.2  # Velocidade angular de 0.2 rad/s

    try:
        rclpy.spin(controlador)
    except KeyboardInterrupt:
        pass

    controlador.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
