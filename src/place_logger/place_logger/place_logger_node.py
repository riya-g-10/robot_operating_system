import rclpy
from rclpy.node import Node

class PlaceLogger(Node):
    def __init__(self):
        super().__init__('place_logger')

    def run(self):
        file = open("visited_places.txt", "a")

        while True:
            place = input("Which place did you visit in IIT Bombay? (type 'exit' to quit): ")

            if place.lower() == "exit":
                break

            file.write(place + "\n")
            print("Saved!")

        file.close()
        self.get_logger().info("Shutting down...")

def main(args=None):
    rclpy.init(args=args)

    node = PlaceLogger()
    node.run()          # Start the interaction

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()