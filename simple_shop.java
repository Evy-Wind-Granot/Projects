public class Order {
    boolean isFilled;
    double billAmount;
    String shipping;
    
    public Order(boolean filled, double cost, String shippingMethod) {
      if (cost > 24.00) {
        System.out.println("High value item!");
      } else {
        System.out.println("Low value item!");
      }
      isFilled = filled;
      billAmount = cost;
      shipping = shippingMethod;
    }
    
    public void ship() {
      if (isFilled) {
        System.out.println("Shipping");
      } else {
        System.out.println("Order not ready");
      }
      
      double shippingCost = calculateShipping();
      
      System.out.println("Shipping cost: ");
      System.out.println(shippingCost);
    }
    
    public double calculateShipping() {
      double shippingCost;
      switch (shipping) {
        case "Regular":
          shippingCost = 0;
          break;
        case "Express":    
          shippingCost = 1.75;
          break;
        default:
          shippingCost = .50; 
      }
      return shippingCost;
    }
    
    public static void main(String[] args) {
      // Create instances and call methods here!
      Order order1 = new Order(true, 30.00, "Regular");
      order1.ship();
      
      System.out.println("-------------------------");
      
      Order order2 = new Order(false, 15.00, "Express");
      order2.ship();
      
      System.out.println("-------------------------");
      
      Order order3 = new Order(true, 10.00, "Standard");
      order3.ship();
    }
  }