import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class LeituraObstaculos(Node):
    def __init__(self):
        super().__init__('LeituraObstaculos')
        self.posicao_carrinhox = None
        self.posicao_obsx = None

    def assinatura(self, alvo):
        assinatura = self.create_subscription(
            Odometry,
            f'/alvo{alvo}/odometry',
            lambda msg, alvo=alvo: self.coordenadas_callback(msg, alvo),
            10
        )
        return assinatura
    
    def assinatura_carrinho(self):
        assinatura = self.create_subscription(
            Odometry,
            '/carrinho/odometry',
            self.coordenadas_carrinho_callback,
            10
        )
        return assinatura

    def coordenadas_callback(self, msg, alvo):
        self.posicao_obsx = msg.pose.pose.position.x
        self.get_logger().info(f'Mensagem da posição do alvo {alvo} recebida!')

    def coordenadas_carrinho_callback(self, msg):
        self.posicao_carrinhox = msg.pose.pose.position.x
        self.get_logger().info('Mensagem da posição do carrinho recebida!')

def main():
    rclpy.init()
    leitura = LeituraObstaculos()

    for alvo in range(1,6):
        leitura.assinatura(alvo)
    
    leitura.assinatura_carrinho()

    try:
        rclpy.spin(leitura)
    except KeyboardInterrupt:
            pass

    leitura.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 
